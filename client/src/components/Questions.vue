<template>
<div class="container">
    <h1>Interrogatório Criminal</h1>
    <div v-if="this.questStart===false" class="container my-5">
        <h2>Um crime foi cometido responda o questionário
        para colaborar com a investigação.</h2>
        <button
        type="button"
        class="btn btn-success mt-4"
        v-on:click.stop.prevent = startQuest
        >Iniciar</button>
    </div>
    <div v-else class="container my-5">
        <div class="row">
            <div class="col"></div>
            <div class="col-8 text-center">
                <h2>{{questions[index]}}</h2>
                <button type="button"
                class="btn btn-success
                float-right mt-5"
                v-on:click.stop.prevent = getAnswerYes
                >Sim</button>
                <button type="button"
                class="btn btn-danger
                float-right mt-5"
                v-on:click.stop.prevent = getAnswerNo
                >Não</button>
            </div>
            <div class="col"></div>
        </div>
    </div>
</div>
</template>

<script>

export default {
  data() {
    return {
      questStart: false,
      questions: ['Telefonou para a vítima?',
        'Esteve no local do Crime?',
        'Mora perto da vítima?',
        'Devia para a vítima?',
        'Já trabalhou com a vítima?'],
      index: 0,
      answers: [],
    };
  },

  methods: {
    startQuest() {
      this.questStart = true;
    },
    nextQuest() {
      this.index += 1;
    },
    getAnswerYes() {
      this.answers.push('sim');
      console.log(this.answers);
      this.nextQuest();
    },
    getAnswerNo() {
      this.answers.push('nao');
      console.log(this.answers);
      this.nextQuest();
    },
  },
};
</script>
