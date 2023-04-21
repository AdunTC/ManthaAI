<script>
    // import store data
    import {pageStore} from "../data/stores"

    // functions
    const menuItems = ["Desk", "Response Configuration", "Plot", "Character", "Author's Note"]
    export let activeItem = menuItems[0]
    const setActive = (item) => {
        activeItem = item;
        pageStore.set(item);
    }
    
</script>

<style>
    #title {
        color: gold;
        font-size: 30px;
        text-align: left;
    }
    button {
        color: white;
        background-color: transparent;
        border: none;
    }
    button:hover {
        color: gold;
    }
    button.menu-item:hover:not(.active) {
        background-color: transparent;
    }
    .active {
        background-color: rgb(100, 120, 170);
    }
    .active:hover {
        color: white;
    }
</style>

<div class="header">
    <div class="right-box" id="title">MANTHA AI</div>
    <hr>
    <div id="header-menu">
        {#each menuItems as item}
            <button on:click={() => setActive(item)} class="menu-item:selected={item === activeItem} {item === activeItem ? 'active' : ''}">{item}</button>
        {/each}
    </div>
</div>