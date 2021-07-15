<template>
<div class="container">
    <div v-if="this.questStart===false" class="container my-5">
        <h1>Interrogatório Criminal</h1>
        <h2 class="mt-5">Um crime foi cometido. Insira seu nome e responda o questionário
        para colaborar com a investigação.</h2>
        <button
        type="button"
        class="btn btn-success mt-4 btn-lg"
        v-on:click.stop.prevent = startQuest
        >Iniciar</button>
    </div>
    <transition name="fade">
    <div v-if="this.questStart && this.questFinish == false"
    class="container my-5">
        <div class="row">
            <div class="col"></div>
            <div class="col-8">
                <h1>Questão {{this.index + 1}}</h1>
                <h2 class="text-center mt-5">{{questions[index]}}</h2>
                <div class="float-right">
                    <button type="button"
                    class="btn btn-success
                    mt-5 mr-3 btn-lg"
                    v-on:click.stop.prevent = getAnswerYes
                    >Sim</button>
                    <button type="button"
                    class="btn btn-danger
                    mt-5 mr-2 btn-lg"
                    v-on:click.stop.prevent = getAnswerNo
                    >Não</button>
                </div>
            </div>
            <div class="col"></div>
        </div>
    </div>
    </transition>
    <div v-if="this.questFinish" class="container mt-5 text-center">
        <h1>Resultado</h1>
        <h2 class="mt-5">{{result}}</h2>
    </div>
</div>
</template>

<script>

export default {
  data() {
    return {
      questStart: false,
      questFinish: false,
      questions: ['Telefonou para a vítima?',
        'Esteve no local do Crime?',
        'Mora perto da vítima?',
        'Devia para a vítima?',
        'Já trabalhou com a vítima?'],
      index: 0,
      answers: [],
      result: '',
    };
  },

  methods: {
    startQuest() {
      this.questStart = true;
    },
    nextQuest() {
      this.index += 1;
      if (this.index === 5) {
        this.questFinished();
      }
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
    questFinished() {
      this.questFinish = true;
      this.questResult();
    },
    questResult() {
      let answers = 0;
      let aux = this.answers.indexOf('sim');
      while (aux !== -1) {
        answers += 1;
        aux = this.answers.indexOf('sim', aux + 1);
      }
      if (answers === 2) {
        this.result = 'Suspeito';
      }
      if (answers >= 3 || answers <= 4) {
        this.result = 'Cúmplice';
      }
      if (answers === 5) {
        this.result = 'Assassino';
      }
      if (answers === 0) {
        this.result = 'Inocente';
      }
    },
  },
};
</script>

<style>
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
