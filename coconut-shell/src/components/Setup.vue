<template>
    <div class="container" v-if="setup === 1">
        <div class="setup-header">
            <Logo />
            <h1>Create Login < Setup</h1>
            <p>Create an Admin user to login to Coconut.
                <br>After setup is complete, you can add more users at the configuration page.
            </p>
        </div>
        <CreateUser />
        <div class="separator"></div>
        <div class="setup-controls">
            <button @click="nextStep" class="btn btn-success">Next</button>
        </div>
    </div>

    <div class="container" v-else-if="setup === 2">
        <div class="setup-header">
            <Logo />
            <h1>Select Modules < Setup</h1>
            <p>Select the modules you want to use in Coconut and the order they should appear.
                <br>You can always change this later in the configuration page.
            </p>
        </div>
        <ModuleSelection />
        <div class="separator"></div>
        <div class="setup-controls">
            <button @click="previousStep" class="btn">Back</button>
            <button @click="nextStep" class="btn btn-success">Next</button>
        </div>
    </div>

    <div class="container" v-else-if="setup === 3">
        <div class="setup-header">
            <Logo />
            <h1>Create Backup < Setup</h1>
            <p>Create automatic backups. Backups without a schedule can be created manually.</p>
        </div>
        <CreateBackup />
        <div class="separator"></div>
        <div class="setup-controls">
            <button @click="previousStep" class="btn">Back</button>
            <button @click="nextStep" class="btn btn-success">Next</button>
        </div>
    </div>

    <div class="container" v-else>
        <div class="setup-header">
            <Logo />
            <h1>Finish < Setup</h1>
                    <p>Setup is complete! You can now finish the setup and start using Coconut.</p>
        </div>
        <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
        <div class="separator"></div>
        <div class="setup-controls">
            <button @click="previousStep" class="btn">Back</button>
            <button @click="finishSetup" class="btn btn-success setup-finish-btn"
                title="Click to finish the setup">Finish Setup</button>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { getCsrfToken } from '@/csrf';
import Logo from './Logo.vue';

import CreateUser from './setup/CreateUser.vue';
import ModuleSelection from './setup/ModuleSelection.vue';
import CreateBackup from './setup/CreateBackup.vue';

const router = useRouter();
const setup = ref<number>(1);
const csrfToken = ref<string>('');
const modules = ref<string[]>([]);

const nextStep = () => {
    setup.value += 1;
}

const previousStep = () => {
    setup.value -= 1;
}

const finishSetup = async () => {
    try {
        const token = await getCsrfToken();

        const response = await fetch('/setup/finish', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': token
            }
        });
        const data = await response.json();
        if (data.success) {
            router.push('/login');
        } else {
            alert(data.message);
        }
    } catch (error) {
        alert('An error occurred while finishing the setup.');
        console.error('Error:', error);
    }
}
</script>
