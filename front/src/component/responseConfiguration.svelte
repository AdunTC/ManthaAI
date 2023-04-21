<script>
    // import svelte libs
    import { onMount, onDestroy } from "svelte";

    // import libs
    import {tokenize} from "sbd";

    // value vars
    let temperatureValue = 0.9;
    let frequencyPenaltyValue = 0.5;
    let presencePenaltyValue = 0.5;

    let mainPrompt_text = "";
    let firstDescription_text = "";
    let mainPrompt_tokens = 0;
    let firstDescription_tokens = 0;
    
    // countTokens
    const countTokens = (name) => {
        if (name = "MP") {
            mainPrompt_tokens = mainPrompt_text.length;
        }
        if (name = "FD") {
            firstDescription_tokens = firstDescription_text.length;
        }
        
    }

    // handleInput
    const handleInput_Temperature = (event) => {
        temperatureValue = Number(event.target.value);
    }
    const handleInput_FrequencyPenalty = (event) => {
        frequencyPenaltyValue = Number(event.target.value);
    }
    const handleInput_PresencePenalty = (event) => {
        presencePenaltyValue = Number(event.target.value);
    }

    // reset
    const resetValue = () => {
        temperatureValue = 0.9;
        frequencyPenaltyValue = 0.5;
        presencePenaltyValue = 0.5;
    }

    // onMount - onDestroy
    onMount(() => {
        const savedTemperatureValue = localStorage.getItem("temperatureValue");
        const savedFrequencyPenaltyValue = localStorage.getItem("frequencyPenaltyValue");
        const savedPresencePenaltyValue = localStorage.getItem("presencePenaltyValue");

        if (savedTemperatureValue) {
            temperatureValue = Number(savedTemperatureValue);
            document.querySelector("#temperature-bar").value = temperatureValue;
        }
        if (savedFrequencyPenaltyValue) {
            frequencyPenaltyValue = Number(savedFrequencyPenaltyValue);
            document.querySelector("#frequencyPenalty-bar").value = frequencyPenaltyValue;
        }
        if (savedPresencePenaltyValue) {
            presencePenaltyValue = Number(savedPresencePenaltyValue);
            document.querySelector("#presencePenalty-bar").value = presencePenaltyValue;
        }
    });
    onDestroy(() => {
        localStorage.setItem('temperatureValue', temperatureValue);
        localStorage.setItem('frequencyPenaltyValue', frequencyPenaltyValue);
        localStorage.setItem('presencePenaltyValue', presencePenaltyValue);
    });
</script>
  
<style>
    .slider {
        -webkit-appearance: none;
        width: 100%;
        height: 10px;
        border-radius: 5px;
        background: rgba(255, 255, 255, 10%);
        outline: none;
        border: none;
    }
    
    .slider::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 11px;
        height: 11px;
        border-radius: 50%;
        background: rgba(255, 255, 255, 75%);
        cursor: pointer;
    }
    
    .response-menu {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
    }

    .prompt-input {
        color: white;
        background-color: rgba(255, 255, 255, 10%);
        border: none;
        outline: none;
        width: 100%;
        height: 100px;
        font-size: 15px;
        resize: vertical;
    }
        
</style>
  
<div id="response-slider">
    <!-- Temperature -->
    <div class="response-menu">Temperature</div>
    <input type="range" class="slider" id="temperature-bar" on:input={handleInput_Temperature} min=0.01 max=2.00 step=0.01 value={temperatureValue}/>
    <div class="right-box">{temperatureValue.toFixed(2)}</div>

    <!-- Frequency Penalty -->
    <div class="response-menu">Frequency Penalty</div>
    <input type="range" class="slider" id="frequencyPenalty-bar" on:input={handleInput_FrequencyPenalty} min=0.01 max=2.00 step=0.01 value={frequencyPenaltyValue}/>
    <div class="right-box">{frequencyPenaltyValue.toFixed(2)}</div>

    <!-- Frequency Penalty -->
    <div class="response-menu">Presence Penalty</div>
    <input type="range" class="slider" id="presencePenalty-bar" on:input={handleInput_PresencePenalty} min=0.01 max=2.00 step=0.01 value={presencePenaltyValue}/>
    <div class="right-box">{presencePenaltyValue.toFixed(2)}</div>

    <!-- Reset Button -->
    <p class="right-box"><button class="red-button" on:click={resetValue}>Reset</button></p>

    <!-- Main Prompt -->
    <div class="response-menu">Main Prompt</div>
    <textarea class="prompt-input" id="main-prompt" bind:value={mainPrompt_text} on:input={() => countTokens("MP")}></textarea><br>
    <div class="right-box">[{mainPrompt_tokens} tokens]</div>

    <!-- First Description -->
    <div class="response-menu">First Description</div>
    <textarea class="prompt-input" id="first-description" bind:value={firstDescription_text} on:input={() => countTokens("FD")}></textarea><br>
    <div class="right-box">[{firstDescription_tokens} tokens]</div>

    <!-- Save Preset -->
    <p class="right-box">
        <button class="yellow-button">Import Preset</button>
        <button class="green-button">Save Preset</button>
    </p>
</div>