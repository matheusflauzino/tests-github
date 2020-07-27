<template>
  <layout>
    <div slot="content">
      <div class="row">
        <div class="col-4">
          <img alt="Vue logo" src="../assets/github.png" class="img-fluid" />
        </div>
        <div class="col">
          <h1 class="my-4 text-left">Analyze the expert tester of a project on Github</h1>
        </div>
      </div>
      <div class="row">
        <div class="col">
          <form class="form-inline my-2 my-lg-0" @submit.prevent="analyze">
            <div class="form-group col-sm-10">
              <input
                class="form-control w-100 mr-sm-2"
                type="text"
                placeholder="url repository"
                aria-label="Search"
                v-model="form.repository"
              />
            </div>
            <div class="form-group col-sm-2">
              <button class="btn btn-outline-success my-2 my-sm-0 btn-block" type="submit">Analyze</button>
            </div>
          </form>
        </div>
      </div>

      <div class="row p-4" v-if="vizible">
        <div class="col-4">
          <h4>Contribuitions Distribuitions</h4>
          <apexchart
            width="100%"
            type="line"
            :options="chartContribuitions.options"
            :series="chartContribuitions.series"
          ></apexchart>
        </div>
        <div class="col-4">
          <h4>Contribuitions Users</h4>
          <apexchart
            width="380"
            type="donut"
            :options="chartUser.options"
            :series="chartUser.series"
          ></apexchart>
        </div>
        <div class="col-4">
          <h4>Contribuitions Testers</h4>
          <apexchart
            width="380"
            type="donut"
            :options="chartUserTesters.options"
            :series="chartUserTesters.series"
          ></apexchart>
        </div>
      </div>
      <div class="row">
        <div class="col p-4">
          <table class="table">
            <thead>
              <tr>
                <th>Date</th>
                <th>Hash</th>
                <th>Author</th>
                <th>Path</th>
                <th class="text-center">Added</th>
                <th class="text-center">Removed</th>
                <th class="text-center">Is test</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(item, index) in contribuitions.data" :key="index">
                <td>{{ item.date }}</td>
                <td>{{ item.hash }}</td>
                <td>{{ item.author }}</td>
                <td>{{ item.path }}</td>
                <td class="text-center">
                  <span class="badge badge-success">{{ item.added }}</span>
                </td>
                <td class="text-center">
                  <span class="badge badge-danger">{{ item.removed }}</span>
                </td>
                <td class="text-center">
                  <span
                    class="badge"
                    :class="item.is_test ? 'badge-success' : 'badge-danger'"
                  >{{ item.is_test ? 'yes' : 'no' }}</span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </layout>
</template>

<script>
// @ is an alias to /src
import Layout from "@/layouts/Layout";
import axios from "axios";
import VueApexCharts from "vue-apexcharts";

export default {
  name: "Home",
  components: {
    Layout,
    apexchart: VueApexCharts
  },

  data() {
    return {
      form: {
        repository: "" //exemplo: git@github.com:matheusflauzino/poc.git
      },

      vizible: false,

      contribuitions: [],

      //teste computeer
      chartContribuitions: {
        options: {
          chart: {
            id: "vuechart-example"
          },
          xaxis: {
            categories: []
          },
          colors: ["#28a745", "#E91E63"]
        },
        series: [
          {
            name: "added",
            data: []
          },
          {
            name: "removed",
            data: []
          }
        ]
      },

      //users
      chartUser: {
        options: {
          labels: []
        },
        series: []
      },

      chartUserTesters: {
        options: {
          labels: []
        },
        series: []
      }
    };
  },

  methods: {
    analyze: async function() {
      let data = await axios.post(
        "http://localhost:5000/contribuitions",
        this.form
      );

      this.contribuitions = data.data;

      this.vizible = true;

      let dates = [];
      let added = [];
      let removed = [];
      if (this.contribuitions.data.length > 0) {
        this.contribuitions.data.map(function(item) {
          dates.push(item.date);
          added.push(item.added);
          removed.push(item.removed);
        });

        this.chartContribuitions.options.xaxis.categories = dates;
        this.chartContribuitions.series = [{ data: added }, { data: removed }];
      }

      //moke
      this.chartUser.series = [...data.data.users];
      this.chartUser.options.labels = [...data.data.users];

      //moke
      this.chartUserTesters.series = [...data.data.testers];
      this.chartUserTesters.options.labels = [...data.data.testers];
    }
  },

  computer: {}
};
</script>
