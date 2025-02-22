Devops 
======

.. autosummary::
    :toctree: devops/client
    :nosignatures:
    :template: autosummary/service_client.rst

    oci.devops.DevopsClient
    oci.devops.DevopsClientCompositeOperations

--------
 Models
--------

.. autosummary::
    :toctree: devops/models
    :nosignatures:
    :template: autosummary/model_class.rst

    oci.devops.models.AbsoluteWaitCriteria
    oci.devops.models.AbsoluteWaitCriteriaSummary
    oci.devops.models.ActualBuildRunnerShapeConfig
    oci.devops.models.ApprovalAction
    oci.devops.models.ApprovalPolicy
    oci.devops.models.ApproveDeploymentDetails
    oci.devops.models.AutomatedDeployStageRollbackPolicy
    oci.devops.models.BackendSetIpCollection
    oci.devops.models.BuildOutputs
    oci.devops.models.BuildPipeline
    oci.devops.models.BuildPipelineCollection
    oci.devops.models.BuildPipelineParameter
    oci.devops.models.BuildPipelineParameterCollection
    oci.devops.models.BuildPipelineStage
    oci.devops.models.BuildPipelineStageCollection
    oci.devops.models.BuildPipelineStagePredecessor
    oci.devops.models.BuildPipelineStagePredecessorCollection
    oci.devops.models.BuildPipelineStageRunProgress
    oci.devops.models.BuildPipelineStageSummary
    oci.devops.models.BuildPipelineSummary
    oci.devops.models.BuildRun
    oci.devops.models.BuildRunArgument
    oci.devops.models.BuildRunArgumentCollection
    oci.devops.models.BuildRunProgress
    oci.devops.models.BuildRunProgressSummary
    oci.devops.models.BuildRunSource
    oci.devops.models.BuildRunSummary
    oci.devops.models.BuildRunSummaryCollection
    oci.devops.models.BuildSource
    oci.devops.models.BuildSourceCollection
    oci.devops.models.BuildStage
    oci.devops.models.BuildStageRunProgress
    oci.devops.models.BuildStageRunStep
    oci.devops.models.BuildStageSummary
    oci.devops.models.CancelBuildRunDetails
    oci.devops.models.CancelDeploymentDetails
    oci.devops.models.ChangeProjectCompartmentDetails
    oci.devops.models.CommitInfo
    oci.devops.models.ComputeInstanceGroupBlueGreenDeployStage
    oci.devops.models.ComputeInstanceGroupBlueGreenDeployStageExecutionProgress
    oci.devops.models.ComputeInstanceGroupBlueGreenDeployStageSummary
    oci.devops.models.ComputeInstanceGroupBlueGreenTrafficShiftDeployStage
    oci.devops.models.ComputeInstanceGroupBlueGreenTrafficShiftDeployStageExecutionProgress
    oci.devops.models.ComputeInstanceGroupBlueGreenTrafficShiftDeployStageSummary
    oci.devops.models.ComputeInstanceGroupByIdsSelector
    oci.devops.models.ComputeInstanceGroupByQuerySelector
    oci.devops.models.ComputeInstanceGroupCanaryApprovalDeployStage
    oci.devops.models.ComputeInstanceGroupCanaryApprovalDeployStageExecutionProgress
    oci.devops.models.ComputeInstanceGroupCanaryApprovalDeployStageSummary
    oci.devops.models.ComputeInstanceGroupCanaryDeployStage
    oci.devops.models.ComputeInstanceGroupCanaryDeployStageExecutionProgress
    oci.devops.models.ComputeInstanceGroupCanaryDeployStageSummary
    oci.devops.models.ComputeInstanceGroupCanaryTrafficShiftDeployStage
    oci.devops.models.ComputeInstanceGroupCanaryTrafficShiftDeployStageExecutionProgress
    oci.devops.models.ComputeInstanceGroupCanaryTrafficShiftDeployStageSummary
    oci.devops.models.ComputeInstanceGroupDeployEnvironment
    oci.devops.models.ComputeInstanceGroupDeployEnvironmentSummary
    oci.devops.models.ComputeInstanceGroupDeployStage
    oci.devops.models.ComputeInstanceGroupDeployStageExecutionProgress
    oci.devops.models.ComputeInstanceGroupDeployStageSummary
    oci.devops.models.ComputeInstanceGroupFailurePolicy
    oci.devops.models.ComputeInstanceGroupFailurePolicyByCount
    oci.devops.models.ComputeInstanceGroupFailurePolicyByPercentage
    oci.devops.models.ComputeInstanceGroupLinearRolloutPolicyByCount
    oci.devops.models.ComputeInstanceGroupLinearRolloutPolicyByPercentage
    oci.devops.models.ComputeInstanceGroupRolloutPolicy
    oci.devops.models.ComputeInstanceGroupSelector
    oci.devops.models.ComputeInstanceGroupSelectorCollection
    oci.devops.models.Connection
    oci.devops.models.ConnectionCollection
    oci.devops.models.ConnectionSummary
    oci.devops.models.ContainerRegistryDeliveredArtifact
    oci.devops.models.CountBasedApprovalPolicy
    oci.devops.models.CreateAbsoluteWaitCriteriaDetails
    oci.devops.models.CreateBuildPipelineDetails
    oci.devops.models.CreateBuildPipelineStageDetails
    oci.devops.models.CreateBuildRunDetails
    oci.devops.models.CreateBuildStageDetails
    oci.devops.models.CreateComputeInstanceGroupBlueGreenDeployStageDetails
    oci.devops.models.CreateComputeInstanceGroupBlueGreenTrafficShiftDeployStageDetails
    oci.devops.models.CreateComputeInstanceGroupCanaryApprovalDeployStageDetails
    oci.devops.models.CreateComputeInstanceGroupCanaryDeployStageDetails
    oci.devops.models.CreateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails
    oci.devops.models.CreateComputeInstanceGroupDeployEnvironmentDetails
    oci.devops.models.CreateComputeInstanceGroupDeployStageDetails
    oci.devops.models.CreateConnectionDetails
    oci.devops.models.CreateDeliverArtifactStageDetails
    oci.devops.models.CreateDeployArtifactDetails
    oci.devops.models.CreateDeployEnvironmentDetails
    oci.devops.models.CreateDeployPipelineDeploymentDetails
    oci.devops.models.CreateDeployPipelineDetails
    oci.devops.models.CreateDeployPipelineRedeploymentDetails
    oci.devops.models.CreateDeployStageDetails
    oci.devops.models.CreateDeploymentDetails
    oci.devops.models.CreateDevopsCodeRepositoryTriggerDetails
    oci.devops.models.CreateFunctionDeployEnvironmentDetails
    oci.devops.models.CreateFunctionDeployStageDetails
    oci.devops.models.CreateGithubAccessTokenConnectionDetails
    oci.devops.models.CreateGithubTriggerDetails
    oci.devops.models.CreateGitlabAccessTokenConnectionDetails
    oci.devops.models.CreateGitlabTriggerDetails
    oci.devops.models.CreateInvokeFunctionDeployStageDetails
    oci.devops.models.CreateLoadBalancerTrafficShiftDeployStageDetails
    oci.devops.models.CreateManualApprovalDeployStageDetails
    oci.devops.models.CreateOkeBlueGreenDeployStageDetails
    oci.devops.models.CreateOkeBlueGreenTrafficShiftDeployStageDetails
    oci.devops.models.CreateOkeCanaryApprovalDeployStageDetails
    oci.devops.models.CreateOkeCanaryDeployStageDetails
    oci.devops.models.CreateOkeCanaryTrafficShiftDeployStageDetails
    oci.devops.models.CreateOkeClusterDeployEnvironmentDetails
    oci.devops.models.CreateOkeDeployStageDetails
    oci.devops.models.CreateProjectDetails
    oci.devops.models.CreateRepositoryDetails
    oci.devops.models.CreateSingleDeployStageDeploymentDetails
    oci.devops.models.CreateSingleDeployStageRedeploymentDetails
    oci.devops.models.CreateTriggerDeploymentStageDetails
    oci.devops.models.CreateTriggerDetails
    oci.devops.models.CreateWaitCriteriaDetails
    oci.devops.models.CreateWaitDeployStageDetails
    oci.devops.models.CreateWaitStageDetails
    oci.devops.models.DeliverArtifact
    oci.devops.models.DeliverArtifactCollection
    oci.devops.models.DeliverArtifactStage
    oci.devops.models.DeliverArtifactStageRunProgress
    oci.devops.models.DeliverArtifactStageSummary
    oci.devops.models.DeliveredArtifact
    oci.devops.models.DeliveredArtifactCollection
    oci.devops.models.DeployArtifact
    oci.devops.models.DeployArtifactCollection
    oci.devops.models.DeployArtifactOverrideArgument
    oci.devops.models.DeployArtifactOverrideArgumentCollection
    oci.devops.models.DeployArtifactSource
    oci.devops.models.DeployArtifactSummary
    oci.devops.models.DeployEnvironment
    oci.devops.models.DeployEnvironmentCollection
    oci.devops.models.DeployEnvironmentSummary
    oci.devops.models.DeployPipeline
    oci.devops.models.DeployPipelineArtifact
    oci.devops.models.DeployPipelineArtifactCollection
    oci.devops.models.DeployPipelineCollection
    oci.devops.models.DeployPipelineDeployment
    oci.devops.models.DeployPipelineDeploymentSummary
    oci.devops.models.DeployPipelineEnvironment
    oci.devops.models.DeployPipelineEnvironmentCollection
    oci.devops.models.DeployPipelineParameter
    oci.devops.models.DeployPipelineParameterCollection
    oci.devops.models.DeployPipelineRedeployment
    oci.devops.models.DeployPipelineRedeploymentSummary
    oci.devops.models.DeployPipelineStage
    oci.devops.models.DeployPipelineStageCollection
    oci.devops.models.DeployPipelineSummary
    oci.devops.models.DeployStage
    oci.devops.models.DeployStageCollection
    oci.devops.models.DeployStageExecutionProgress
    oci.devops.models.DeployStageExecutionProgressDetails
    oci.devops.models.DeployStageExecutionStep
    oci.devops.models.DeployStagePredecessor
    oci.devops.models.DeployStagePredecessorCollection
    oci.devops.models.DeployStageRollbackPolicy
    oci.devops.models.DeployStageSummary
    oci.devops.models.Deployment
    oci.devops.models.DeploymentArgument
    oci.devops.models.DeploymentArgumentCollection
    oci.devops.models.DeploymentCollection
    oci.devops.models.DeploymentExecutionProgress
    oci.devops.models.DeploymentSummary
    oci.devops.models.DevopsCodeRepositoryBuildRunSource
    oci.devops.models.DevopsCodeRepositoryBuildSource
    oci.devops.models.DevopsCodeRepositoryFilter
    oci.devops.models.DevopsCodeRepositoryFilterAttributes
    oci.devops.models.DevopsCodeRepositoryTrigger
    oci.devops.models.DevopsCodeRepositoryTriggerCreateResult
    oci.devops.models.DevopsCodeRepositoryTriggerSummary
    oci.devops.models.DiffChunk
    oci.devops.models.DiffCollection
    oci.devops.models.DiffLineDetails
    oci.devops.models.DiffResponse
    oci.devops.models.DiffResponseEntry
    oci.devops.models.DiffSection
    oci.devops.models.DiffSummary
    oci.devops.models.ExportedVariable
    oci.devops.models.ExportedVariableCollection
    oci.devops.models.FileDiffResponse
    oci.devops.models.FileLineDetails
    oci.devops.models.Filter
    oci.devops.models.FunctionDeployEnvironment
    oci.devops.models.FunctionDeployEnvironmentSummary
    oci.devops.models.FunctionDeployStage
    oci.devops.models.FunctionDeployStageExecutionProgress
    oci.devops.models.FunctionDeployStageSummary
    oci.devops.models.GenericDeliveredArtifact
    oci.devops.models.GenericDeployArtifactSource
    oci.devops.models.GithubAccessTokenConnection
    oci.devops.models.GithubAccessTokenConnectionSummary
    oci.devops.models.GithubBuildRunSource
    oci.devops.models.GithubBuildSource
    oci.devops.models.GithubFilter
    oci.devops.models.GithubFilterAttributes
    oci.devops.models.GithubTrigger
    oci.devops.models.GithubTriggerCreateResult
    oci.devops.models.GithubTriggerSummary
    oci.devops.models.GitlabAccessTokenConnection
    oci.devops.models.GitlabAccessTokenConnectionSummary
    oci.devops.models.GitlabBuildRunSource
    oci.devops.models.GitlabBuildSource
    oci.devops.models.GitlabFilter
    oci.devops.models.GitlabFilterAttributes
    oci.devops.models.GitlabTrigger
    oci.devops.models.GitlabTriggerCreateResult
    oci.devops.models.GitlabTriggerSummary
    oci.devops.models.InlineDeployArtifactSource
    oci.devops.models.InvokeFunctionDeployStage
    oci.devops.models.InvokeFunctionDeployStageExecutionProgress
    oci.devops.models.InvokeFunctionDeployStageSummary
    oci.devops.models.LoadBalancerConfig
    oci.devops.models.LoadBalancerTrafficShiftDeployStage
    oci.devops.models.LoadBalancerTrafficShiftDeployStageExecutionProgress
    oci.devops.models.LoadBalancerTrafficShiftDeployStageSummary
    oci.devops.models.LoadBalancerTrafficShiftRolloutPolicy
    oci.devops.models.ManualApprovalDeployStage
    oci.devops.models.ManualApprovalDeployStageExecutionProgress
    oci.devops.models.ManualApprovalDeployStageSummary
    oci.devops.models.ManualBuildRunSource
    oci.devops.models.MirrorRepositoryConfig
    oci.devops.models.NetworkChannel
    oci.devops.models.NginxBlueGreenStrategy
    oci.devops.models.NginxCanaryStrategy
    oci.devops.models.NoDeployStageRollbackPolicy
    oci.devops.models.NotificationConfig
    oci.devops.models.OcirDeployArtifactSource
    oci.devops.models.OkeBlueGreenDeployStage
    oci.devops.models.OkeBlueGreenDeployStageExecutionProgress
    oci.devops.models.OkeBlueGreenDeployStageSummary
    oci.devops.models.OkeBlueGreenStrategy
    oci.devops.models.OkeBlueGreenTrafficShiftDeployStage
    oci.devops.models.OkeBlueGreenTrafficShiftDeployStageExecutionProgress
    oci.devops.models.OkeBlueGreenTrafficShiftDeployStageSummary
    oci.devops.models.OkeCanaryApprovalDeployStage
    oci.devops.models.OkeCanaryApprovalDeployStageExecutionProgress
    oci.devops.models.OkeCanaryApprovalDeployStageSummary
    oci.devops.models.OkeCanaryDeployStage
    oci.devops.models.OkeCanaryDeployStageExecutionProgress
    oci.devops.models.OkeCanaryDeployStageSummary
    oci.devops.models.OkeCanaryStrategy
    oci.devops.models.OkeCanaryTrafficShiftDeployStage
    oci.devops.models.OkeCanaryTrafficShiftDeployStageExecutionProgress
    oci.devops.models.OkeCanaryTrafficShiftDeployStageSummary
    oci.devops.models.OkeClusterDeployEnvironment
    oci.devops.models.OkeClusterDeployEnvironmentSummary
    oci.devops.models.OkeDeployStage
    oci.devops.models.OkeDeployStageExecutionProgress
    oci.devops.models.OkeDeployStageSummary
    oci.devops.models.PrivateEndpointChannel
    oci.devops.models.Project
    oci.devops.models.ProjectCollection
    oci.devops.models.ProjectSummary
    oci.devops.models.PutRepositoryBranchDetails
    oci.devops.models.PutRepositoryRefDetails
    oci.devops.models.PutRepositoryTagDetails
    oci.devops.models.Repository
    oci.devops.models.RepositoryAuthorCollection
    oci.devops.models.RepositoryAuthorSummary
    oci.devops.models.RepositoryBranch
    oci.devops.models.RepositoryBranchSummary
    oci.devops.models.RepositoryCollection
    oci.devops.models.RepositoryCommit
    oci.devops.models.RepositoryCommitCollection
    oci.devops.models.RepositoryCommitSummary
    oci.devops.models.RepositoryFileLines
    oci.devops.models.RepositoryMirrorRecord
    oci.devops.models.RepositoryMirrorRecordCollection
    oci.devops.models.RepositoryMirrorRecordSummary
    oci.devops.models.RepositoryObject
    oci.devops.models.RepositoryPathCollection
    oci.devops.models.RepositoryPathSummary
    oci.devops.models.RepositoryRef
    oci.devops.models.RepositoryRefCollection
    oci.devops.models.RepositoryRefSummary
    oci.devops.models.RepositorySummary
    oci.devops.models.RepositoryTag
    oci.devops.models.RepositoryTagSummary
    oci.devops.models.SingleDeployStageDeployment
    oci.devops.models.SingleDeployStageDeploymentSummary
    oci.devops.models.SingleDeployStageRedeployment
    oci.devops.models.SingleDeployStageRedeploymentSummary
    oci.devops.models.Trigger
    oci.devops.models.TriggerAction
    oci.devops.models.TriggerBuildPipelineAction
    oci.devops.models.TriggerCollection
    oci.devops.models.TriggerCreateResult
    oci.devops.models.TriggerDeploymentPipelineStageRunProgress
    oci.devops.models.TriggerDeploymentStage
    oci.devops.models.TriggerDeploymentStageSummary
    oci.devops.models.TriggerInfo
    oci.devops.models.TriggerSchedule
    oci.devops.models.TriggerSummary
    oci.devops.models.UpdateAbsoluteWaitCriteriaDetails
    oci.devops.models.UpdateBuildPipelineDetails
    oci.devops.models.UpdateBuildPipelineStageDetails
    oci.devops.models.UpdateBuildRunDetails
    oci.devops.models.UpdateBuildStageDetails
    oci.devops.models.UpdateComputeInstanceGroupBlueGreenDeployStageDetails
    oci.devops.models.UpdateComputeInstanceGroupBlueGreenTrafficShiftDeployStageDetails
    oci.devops.models.UpdateComputeInstanceGroupCanaryApprovalDeployStageDetails
    oci.devops.models.UpdateComputeInstanceGroupCanaryDeployStageDetails
    oci.devops.models.UpdateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails
    oci.devops.models.UpdateComputeInstanceGroupDeployEnvironmentDetails
    oci.devops.models.UpdateComputeInstanceGroupDeployStageDetails
    oci.devops.models.UpdateConnectionDetails
    oci.devops.models.UpdateDeliverArtifactStageDetails
    oci.devops.models.UpdateDeployArtifactDetails
    oci.devops.models.UpdateDeployEnvironmentDetails
    oci.devops.models.UpdateDeployPipelineDeploymentDetails
    oci.devops.models.UpdateDeployPipelineDetails
    oci.devops.models.UpdateDeployPipelineRedeploymentDetails
    oci.devops.models.UpdateDeployStageDetails
    oci.devops.models.UpdateDeploymentDetails
    oci.devops.models.UpdateDevopsCodeRepositoryTriggerDetails
    oci.devops.models.UpdateFunctionDeployEnvironmentDetails
    oci.devops.models.UpdateFunctionDeployStageDetails
    oci.devops.models.UpdateGithubAccessTokenConnectionDetails
    oci.devops.models.UpdateGithubTriggerDetails
    oci.devops.models.UpdateGitlabAccessTokenConnectionDetails
    oci.devops.models.UpdateGitlabTriggerDetails
    oci.devops.models.UpdateInvokeFunctionDeployStageDetails
    oci.devops.models.UpdateLoadBalancerTrafficShiftDeployStageDetails
    oci.devops.models.UpdateManualApprovalDeployStageDetails
    oci.devops.models.UpdateOkeBlueGreenDeployStageDetails
    oci.devops.models.UpdateOkeBlueGreenTrafficShiftDeployStageDetails
    oci.devops.models.UpdateOkeCanaryApprovalDeployStageDetails
    oci.devops.models.UpdateOkeCanaryDeployStageDetails
    oci.devops.models.UpdateOkeCanaryTrafficShiftDeployStageDetails
    oci.devops.models.UpdateOkeClusterDeployEnvironmentDetails
    oci.devops.models.UpdateOkeDeployStageDetails
    oci.devops.models.UpdateProjectDetails
    oci.devops.models.UpdateRepositoryDetails
    oci.devops.models.UpdateSingleDeployStageDeploymentDetails
    oci.devops.models.UpdateSingleDeployStageRedeploymentDetails
    oci.devops.models.UpdateTriggerDeploymentStageDetails
    oci.devops.models.UpdateTriggerDetails
    oci.devops.models.UpdateWaitCriteriaDetails
    oci.devops.models.UpdateWaitDeployStageDetails
    oci.devops.models.UpdateWaitStageDetails
    oci.devops.models.WaitCriteria
    oci.devops.models.WaitCriteriaSummary
    oci.devops.models.WaitDeployStage
    oci.devops.models.WaitDeployStageExecutionProgress
    oci.devops.models.WaitDeployStageSummary
    oci.devops.models.WaitStage
    oci.devops.models.WaitStageRunProgress
    oci.devops.models.WaitStageSummary
    oci.devops.models.WorkRequest
    oci.devops.models.WorkRequestCollection
    oci.devops.models.WorkRequestError
    oci.devops.models.WorkRequestErrorCollection
    oci.devops.models.WorkRequestLogEntry
    oci.devops.models.WorkRequestLogEntryCollection
    oci.devops.models.WorkRequestResource
    oci.devops.models.WorkRequestSummary
