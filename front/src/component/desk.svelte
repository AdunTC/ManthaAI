<script>
    let input_api_key = "";
    let saved_api_key = "";

    const handleChangeValue = (event) => {
        input_api_key = event.target.value;
    }
    const submitApiKey = async() => {
        await fetch("http://localhost:8000/api/get_api_key", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({inputValue: input_api_key}),
        });

        const res = await fetch('http://localhost:8000/api/get_input');
	    const data = await res.json();
	    saved_api_key = data.savedValue;

        const resp2 = await fetch('http://localhost:8000/api/get_resp');
        const data2 = await resp2.json();
	    const printd = data2.response;

        console.log(printd);
    }
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
    <input type="text" id="api-key" on:input={handleChangeValue}>
    {#if saved_api_key != "123"}<img src="./imgs/disconnect-icon.png" alt="disconnected" class="connect-icon">{/if}
    {#if saved_api_key == "123"}<span style="color: greenyellow;">CONNECTED!</span>{/if}
    <div class="right-box">
        <button class="red-button" id="disconnectAPI">Disconnect</button>
        <button class="green-button" id="connectAPI" on:click={submitApiKey}>Connect</button>
    </div><br>
    Still have questions left? :<br>
    Check out built-in help or type /? in any chat.
</div>