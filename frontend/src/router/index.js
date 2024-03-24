import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '../components/HelloWorld'

import PublicLogin from '../components/Public/PublicLogin'
import PublicRegister from '../components/Public/PublicRegister'
import PublicHead from '../components/Public/PublicHead'
import PublicRecommendation from '../components/Public/PublicRecommendation/PublicRecommendation'
import PublicResume from '../components/Public/PublicWarehouse/PublicResume'
import PublicResumeEdit from '../components/Public/PublicWarehouse/PublicResumeEdit'
import PublicRiskPrediction from '../components/Public/PublicDiseaseAnalysis/PublicRiskPrediction'
import PublicAssistanceDiagnosis from '../components/Public/PublicDiseaseAnalysis/PublicAssistanceDiagnosis'
import PublicDiseaseAnalysisParent from '../components/Public/PublicDiseaseAnalysis/PublicDiseaseAnalysisParent'
import PublicWarehouseParent from '../components/Public/PublicWarehouse/PublicWarehouseParent'

import DocterLogin from '../components/Docter/DocterLogin'
import DocterHead from '../components/Docter/DocterHead'
import DocterRegister from '../components/Docter/DocterRegister'
import DocterRecommendation from '../components/Docter/DocterRecommendation/DocterRecommendation'
import DocterPatientData from '../components/Docter/DocterWarehouse/DocterPatientData'
import DocterWarehouseParent from '../components/Docter/DocterWarehouse/DocterWarehouseParent'
import DocterDataset from '../components/Docter/DocterWarehouse/DocterDataset'
import DocterRiskPrediction from '../components/Docter/DocterDiseaseAnalysis/DocterRiskPrediction'
import DocterAssistanceDiagnosis from '../components/Docter/DocterDiseaseAnalysis/DocterAssistanceDiagnosis'
import DocterDiseaseAnalysisParent from '../components/Docter/DocterDiseaseAnalysis/DocterDiseaseAnalysisParent'
import DocterModel from '../components/Docter/DocterWarehouse/DocterModel'
import DocterBoard from '../components/Docter/DocterWarehouse/DocterBoard'
import DocterRiskPredictionGraph from '../components/Docter/DocterDiseaseAnalysis/DocterRiskPredictionGraph'

import ScientistHead from '../components/Scientist/ScientistHead'
import ScientistLogin from '../components/Scientist/ScientistLogin'
import ScientistRegister from '../components/Scientist/ScientistRegister'
import ScientistAssistanceDiagnosisGraph from '../components/Scientist/ScientistDiseaseAnalysis/ScientistAssistanceDiagnosisGraph'
import ScientistAssistanceDiagnosis from '../components/Scientist/ScientistDiseaseAnalysis/ScientistAssistanceDiagnosis'
import ScientistBoard from '../components/Scientist/ScientistWarehouse/ScientistBoard'
import ScientistDataset from '../components/Scientist/ScientistWarehouse/ScientistDataset'
import ScientistModel from '../components/Scientist/ScientistWarehouse/ScientistModel'
import ScientistRecommendation from '../components/Scientist/ScientistRecommendation/ScientistRecommendation'
import ScientistPatientData from '../components/Scientist/ScientistWarehouse/ScientistPatientData'
import ScientistRiskPrediction from '../components/Scientist/ScientistDiseaseAnalysis/ScientistRiskPrediction'
import ScientistRiskPredictionGraph from '../components/Scientist/ScientistDiseaseAnalysis/ScientistRiskPredictionGraph'
import ScientistDiseaseAnalysisParent from '../components/Scientist/ScientistDiseaseAnalysis/ScientistDiseaseAnalysisParent'
import ScientistWarehouseParent from '../components/Scientist/ScientistWarehouse/ScientistWarehouseParent'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/PublicLogin',
      name: 'PublicLogin',
      component: PublicLogin
    },
    {
      path: '/PublicRegister',
      name: 'PublicRegister',
      component: PublicRegister
    },
    {
      path: '/PublicHead',
      name: 'PublicHead',
      component: PublicHead
    },
    {
      path: '/PublicDiseaseAnalysis',
      name: 'PublicDiseaseAnalysis',
      component: PublicDiseaseAnalysisParent,
      children: [
        {
          path: 'PublicAssistanceDiagnosis',
          component: PublicAssistanceDiagnosis
        },
        {
          path: 'PublicRiskPrediction',
          component: PublicRiskPrediction
        }
      ]
    },
    {
      path: '/PublicWarehouse',
      name: 'PublicWarehouse',
      component: PublicWarehouseParent,
      children: [
        {
          path: 'PublicResume',
          name: 'PublicResume',
          component: PublicResume
        },
        {
          path: 'PublicResumeEdit',
          name: 'PublicResumeEdit',
          component: PublicResumeEdit
        }
      ]
    },
    {
      path: '/PublicRecommendation',
      name: 'PublicRecommendation',
      component: PublicRecommendation
    },

    {
      path: '/DocterLogin',
      name: 'DocterLogin',
      component: DocterLogin
    },
    {
      path: '/DocterHead',
      name: 'DocterHead',
      component: DocterHead
    },
    {
      path: '/DocterRegister',
      name: 'DocterRegister',
      component: DocterRegister
    },
    {
      path: '/DocterWarehouse',
      name: 'DocterWarehouse',
      component: DocterWarehouseParent,
      children: [
        {
          path: 'DocterDataset',
          component: DocterDataset
        },
        {
          path: 'DocterPatientData',
          component: DocterPatientData
        },
        {
          path: 'DocterModel',
          component: DocterModel
        },
        {
          path: 'DocterBoard',
          component: DocterBoard
        }
      ]
    },
    {
      path: '/DocterDiseaseAnalysis',
      name: 'DocterDiseaseAnalysis',
      component: DocterDiseaseAnalysisParent,
      children: [
        {
          path: 'DocterAssistanceDiagnosis',
          name: 'DocterAssistanceDiagnosis',
          component: DocterAssistanceDiagnosis
        },
        {
          path: 'DocterRiskPredictionGraph',
          name: 'DocterRiskPredictionGraph',
          component: DocterRiskPredictionGraph
        },
        {
          path: 'DocterRiskPrediction',
          name: 'DocterRiskPrediction',
          component: DocterRiskPrediction
        }
      ]
    },
    {
      path: '/DocterRecommendation',
      name: 'DocterRecommendation',
      component: DocterRecommendation
    },

    {
      path: '/ScientistLogin',
      name: 'ScientistLogin',
      component: ScientistLogin
    },
    {
      path: '/ScientistRegister',
      name: 'ScientistRegister',
      component: ScientistRegister
    },
    {
      path: '/ScientistHead',
      name: 'ScientistHead',
      component: ScientistHead
    },
    {
      path: '/ScientistDiseaseAnalysis',
      name: 'ScientistDiseaseAnalysis',
      component: ScientistDiseaseAnalysisParent,
      children: [
        {
          path: 'ScientistAssistanceDiagnosis',
          name: 'ScientistAssistanceDiagnosis',
          component: ScientistAssistanceDiagnosis
        },
        {
          path: 'ScientistAssistanceDiagnosisGraph',
          name: 'ScientistAssistanceDiagnosisGraph',
          component: ScientistAssistanceDiagnosisGraph
        },
        {
          path: 'ScientistRiskPrediction',
          name: 'ScientistRiskPrediction',
          component: ScientistRiskPrediction
        },
        {
          path: 'ScientistRiskPredictionGraph',
          name: 'ScientistRiskPredictionGraph',
          component: ScientistRiskPredictionGraph
        }
      ]
    },
    {
      path: '/ScientistRecommendation',
      name: 'ScientistRecommendation',
      component: ScientistRecommendation
    },
    {
      path: '/ScientistWarehouse',
      name: 'ScientistWarehouse',
      component: ScientistWarehouseParent,
      children: [
        {
          path: 'ScientistBoard',
          name: 'ScientistBoard',
          component: ScientistBoard
        },
        {
          path: 'ScientistDataset',
          name: 'ScientistDataset',
          component: ScientistDataset
        },
        {
          path: 'ScientistModel',
          name: 'ScientistModel',
          component: ScientistModel
        },
        {
          path: 'ScientistPatientData',
          name: 'ScientistPatientData',
          component: ScientistPatientData
        }
      ]
    }
  ]
})
