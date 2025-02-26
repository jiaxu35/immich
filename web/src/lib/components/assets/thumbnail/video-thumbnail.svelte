<script lang="ts">
	import { Duration } from 'luxon';
	import PauseCircleOutline from 'svelte-material-icons/PauseCircleOutline.svelte';
	import PlayCircleOutline from 'svelte-material-icons/PlayCircleOutline.svelte';
	import AlertCircleOutline from 'svelte-material-icons/AlertCircleOutline.svelte';
	import LoadingSpinner from '$lib/components/shared-components/loading-spinner.svelte';

	export let url: string;
	export let durationInSeconds = 0;
	export let enablePlayback = false;
	export let playbackOnIconHover = false;
	export let showTime = true;
	export let playIcon = PlayCircleOutline;
	export let pauseIcon = PauseCircleOutline;

	let remainingSeconds = durationInSeconds;
	let loading = true;
	let error = false;
	let player: HTMLVideoElement;

	$: if (!enablePlayback) {
		// Reset remaining time when playback is disabled.
		remainingSeconds = durationInSeconds;

		if (player) {
			// Cancel video buffering.
			player.src = '';
		}
	}
</script>

<div
	class="absolute right-0 top-0 text-white text-xs font-medium flex gap-1 place-items-center z-20"
>
	{#if showTime}
		<span class="pt-2">
			{Duration.fromObject({ seconds: remainingSeconds }).toFormat('m:ss')}
		</span>
	{/if}

	<span
		class="pt-2 pr-2"
		on:mouseenter={() => {
			if (playbackOnIconHover) {
				enablePlayback = true;
			}
		}}
		on:mouseleave={() => {
			if (playbackOnIconHover) {
				enablePlayback = false;
			}
		}}
	>
		{#if enablePlayback}
			{#if loading}
				<LoadingSpinner />
			{:else if error}
				<AlertCircleOutline size="24" class="text-red-600" />
			{:else}
				<svelte:component this={pauseIcon} size="24" />
			{/if}
		{:else}
			<svelte:component this={playIcon} size="24" />
		{/if}
	</span>
</div>

{#if enablePlayback}
	<video
		bind:this={player}
		class="w-full h-full object-cover"
		muted
		autoplay
		src={url}
		on:play={() => {
			loading = false;
			error = false;
		}}
		on:error={() => {
			error = true;
			loading = false;
		}}
		on:timeupdate={({ currentTarget }) => {
			const remaining = currentTarget.duration - currentTarget.currentTime;
			remainingSeconds = Math.min(Math.ceil(remaining), durationInSeconds);
		}}
	/>
{/if}
