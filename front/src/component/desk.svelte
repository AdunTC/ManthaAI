<script>
    
</script>

<style>
    .text-box {
        text-align: left;
    }
    #api-key {
        width: 100%;
        height: 25px;
        font-size: 15px;
    }
    .connect-icon {
        width: 20px;
        height: 20px;
    }
</style>

<div class="text-box">
    <p><b>Mantha</b></p>
    Welcome to Mantha AI! In order to begin writing the novel :<br>
    <li>Connect to one of the supported generation APIs</li>
    <li>Create or pick the story from the list</li>
    <br>
    <p>Input your API key :</p>
    <input type="text" id="api-key">
    {#if true}
        <img src="./imgs/disconnect-icon.png" alt="disconnected" class="connect-icon">
    {/if}
    <div class="right-box">
        <button class="red-button" id="disconnectAPI">Disconnect</button>
        <button class="green-button" id="connectAPI">Connect</button>
    </div><br>
    Still have questions left? :<br>
    Check out built-in help or type /? in any chat.
</div>