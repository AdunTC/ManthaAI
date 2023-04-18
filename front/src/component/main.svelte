<script>
    // import svelte libs
    import { onMount } from "svelte";
    // import store data
    import { pageStore } from "../data/stores";
    // import svelte components
    import Desk from "./desk.svelte";
    import ResponseConfiguration from "./responseConfiguration.svelte";
    import Result from "./result.svelte";

    // script
    let roomName = "";
    onMount(() => {roomName = "Desk"})
    pageStore.subscribe(value => {roomName = value});
</script>

<style>
    #main-box {
        display: flex;
    }
    #context-box {
        background-color: rgb(70, 90, 130);
        width: 500px;
        height: auto;
        padding: 10px;
        border-radius: 10px;
    }
    #generated-prompt {
        float: left;
        margin-left: 10px;
    }
</style>

<div id="main-box">
    <div id="context-box">
        {#if roomName == "Desk"} <Desk /> {/if}
        {#if roomName == "Response Configuration"} <ResponseConfiguration /> {/if}
    </div>
    <div id="generated-prompt">
        <Result />
    </div>
</div>


