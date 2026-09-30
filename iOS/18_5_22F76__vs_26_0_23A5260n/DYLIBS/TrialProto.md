## TrialProto

> `/System/Library/PrivateFrameworks/TrialProto.framework/TrialProto`

```diff

-429.20.2.0.0
-  __TEXT.__text: 0x58f9c
-  __TEXT.__auth_stubs: 0x780
-  __TEXT.__objc_methlist: 0x7c58
+463.0.0.0.0
+  __TEXT.__text: 0x58dcc
+  __TEXT.__auth_stubs: 0x7a0
+  __TEXT.__objc_methlist: 0x7ad0
   __TEXT.__const: 0x4ef0
-  __TEXT.__cstring: 0x43d3
+  __TEXT.__cstring: 0x427c
   __TEXT.__gcc_except_tab: 0x3b8
-  __TEXT.__unwind_info: 0x1fa0
-  __TEXT.__objc_classname: 0x1481
-  __TEXT.__objc_methname: 0x8248
-  __TEXT.__objc_methtype: 0x1998
-  __TEXT.__objc_stubs: 0x3fa0
-  __DATA_CONST.__got: 0x800
+  __TEXT.__unwind_info: 0x1f18
+  __TEXT.__objc_classname: 0x13f6
+  __TEXT.__objc_methname: 0x7eb5
+  __TEXT.__objc_methtype: 0x1956
+  __TEXT.__objc_stubs: 0x3fc0
+  __DATA_CONST.__got: 0x7b0
   __DATA_CONST.__const: 0xfc8
-  __DATA_CONST.__objc_classlist: 0x720
+  __DATA_CONST.__objc_classlist: 0x6f0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1db0
-  __DATA_CONST.__objc_superrefs: 0x330
-  __AUTH_CONST.__auth_got: 0x3d0
+  __DATA_CONST.__objc_selrefs: 0x1d60
+  __DATA_CONST.__objc_superrefs: 0x328
+  __AUTH_CONST.__auth_got: 0x3e0
   __AUTH_CONST.__const: 0xb0
-  __AUTH_CONST.__cfstring: 0x3060
-  __AUTH_CONST.__objc_const: 0xfa30
-  __AUTH.__objc_data: 0x2d0
-  __AUTH.__data: 0x1418
-  __DATA.__objc_ivar: 0x50c
-  __DATA.__data: 0x1740
-  __DATA.__bss: 0x320
-  __DATA_DIRTY.__objc_data: 0x4470
-  __DATA_DIRTY.__data: 0x4d8
-  __DATA_DIRTY.__bss: 0x208
+  __AUTH_CONST.__cfstring: 0x2fc0
+  __AUTH_CONST.__objc_const: 0xf308
+  __AUTH.__objc_data: 0x230
+  __AUTH.__data: 0x1278
+  __DATA.__objc_ivar: 0x4f8
+  __DATA.__data: 0x16c0
+  __DATA.__bss: 0x2b0
+  __DATA_DIRTY.__objc_data: 0x4330
+  __DATA_DIRTY.__data: 0x490
+  __DATA_DIRTY.__bss: 0x258
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 10CFAC3C-71CE-3925-98F2-B4396F91D801
-  Functions: 2921
-  Symbols:   8484
-  CStrings:  3453
+  UUID: 64B6E90D-5C24-3932-B3B2-A04C5D888718
+  Functions: 2890
+  Symbols:   8374
+  CStrings:  3389
 
Symbols:
+ _OBJC_CLASS_$_TRIMlruntimeEvaluationRoot
+ _OBJC_METACLASS_$_TRIMlruntimeEvaluationRoot
+ _TRIMlruntimeEvaluationRoot_FileDescriptor
+ _TRIMlruntimeEvaluationRoot_FileDescriptor.descriptor
+ __OBJC_CLASS_RO_$_TRIMlruntimeEvaluationRoot
+ __OBJC_METACLASS_RO_$_TRIMlruntimeEvaluationRoot
+ __triNamespaceConversionLock
+ _descriptor.descriptor.28
+ _descriptor.descriptor.78
+ _descriptor.descriptor.93
+ _descriptor.fields.29
+ _descriptor.fields.79
+ _descriptor.fields.94
+ _objc_msgSend$_setError
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$position
+ _objc_msgSend$setPosition:
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- +[TRIBmltDeploymentId descriptor]
- +[TRIClientBackgroundMLTask descriptor]
- +[TRIClientBmltCatalog descriptor]
- +[TRIShadowEvaluation descriptor]
- -[TRITrialBMLTFields .cxx_destruct]
- -[TRITrialBMLTFields clientBmltFactorPackSetId]
- -[TRITrialBMLTFields clientBmltId]
- -[TRITrialBMLTFields clientBmltTargetingRuleGroupOrdinal]
- -[TRITrialBMLTFields copyTo:]
- -[TRITrialBMLTFields copyWithZone:]
- -[TRITrialBMLTFields description]
- -[TRITrialBMLTFields dictionaryRepresentation]
- -[TRITrialBMLTFields hasClientBmltFactorPackSetId]
- -[TRITrialBMLTFields hasClientBmltId]
- -[TRITrialBMLTFields hasClientBmltTargetingRuleGroupOrdinal]
- -[TRITrialBMLTFields hash]
- -[TRITrialBMLTFields isEqual:]
- -[TRITrialBMLTFields mergeFrom:]
- -[TRITrialBMLTFields readFrom:]
- -[TRITrialBMLTFields setClientBmltFactorPackSetId:]
- -[TRITrialBMLTFields setClientBmltId:]
- -[TRITrialBMLTFields setClientBmltTargetingRuleGroupOrdinal:]
- -[TRITrialBMLTFields setHasClientBmltTargetingRuleGroupOrdinal:]
- -[TRITrialBMLTFields writeTo:]
- -[TRITrialSystemTelemetry bmltFields]
- -[TRITrialSystemTelemetry hasBmltFields]
- -[TRITrialSystemTelemetry setBmltFields:]
- -[TRITrialSystemTelemetry(Util) ensureBMLTFields]
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- OBJC_IVAR_$_TRITrialBMLTFields._clientBmltFactorPackSetId
- OBJC_IVAR_$_TRITrialBMLTFields._clientBmltId
- OBJC_IVAR_$_TRITrialBMLTFields._clientBmltTargetingRuleGroupOrdinal
- OBJC_IVAR_$_TRITrialBMLTFields._has
- OBJC_IVAR_$_TRITrialSystemTelemetry._bmltFields
- _OBJC_CLASS_$_TRIBmltDeploymentId
- _OBJC_CLASS_$_TRIClientBackgroundMLTask
- _OBJC_CLASS_$_TRIClientBmltCatalog
- _OBJC_CLASS_$_TRIShadowEvaluation
- _OBJC_CLASS_$_TRITrialBMLTFields
- _OBJC_CLASS_$_TRITriclientBackgroundMltaskRoot
- _OBJC_CLASS_$_TRITrishadowEvaluationRoot
- _OBJC_METACLASS_$_TRIBmltDeploymentId
- _OBJC_METACLASS_$_TRIClientBackgroundMLTask
- _OBJC_METACLASS_$_TRIClientBmltCatalog
- _OBJC_METACLASS_$_TRIShadowEvaluation
- _OBJC_METACLASS_$_TRITrialBMLTFields
- _OBJC_METACLASS_$_TRITriclientBackgroundMltaskRoot
- _OBJC_METACLASS_$_TRITrishadowEvaluationRoot
- _TRIShadowEvaluation_ClearTypeOneOfCase
- _TRITrialBMLTFieldsReadFrom
- _TRITriclientBackgroundMltaskRoot_FileDescriptor
- _TRITriclientBackgroundMltaskRoot_FileDescriptor.descriptor
- _TRITrishadowEvaluationRoot_FileDescriptor
- _TRITrishadowEvaluationRoot_FileDescriptor.descriptor
- __OBJC_$_CLASS_METHODS_TRIBmltDeploymentId
- __OBJC_$_CLASS_METHODS_TRIClientBackgroundMLTask
- __OBJC_$_CLASS_METHODS_TRIClientBmltCatalog
- __OBJC_$_CLASS_METHODS_TRIShadowEvaluation
- __OBJC_$_INSTANCE_METHODS_TRITrialBMLTFields
- __OBJC_$_INSTANCE_VARIABLES_TRITrialBMLTFields
- __OBJC_$_PROP_LIST_TRIBmltDeploymentId
- __OBJC_$_PROP_LIST_TRIClientBackgroundMLTask
- __OBJC_$_PROP_LIST_TRIClientBmltCatalog
- __OBJC_$_PROP_LIST_TRIShadowEvaluation
- __OBJC_$_PROP_LIST_TRITrialBMLTFields
- __OBJC_CLASS_PROTOCOLS_$_TRITrialBMLTFields
- __OBJC_CLASS_RO_$_TRIBmltDeploymentId
- __OBJC_CLASS_RO_$_TRIClientBackgroundMLTask
- __OBJC_CLASS_RO_$_TRIClientBmltCatalog
- __OBJC_CLASS_RO_$_TRIShadowEvaluation
- __OBJC_CLASS_RO_$_TRITrialBMLTFields
- __OBJC_CLASS_RO_$_TRITriclientBackgroundMltaskRoot
- __OBJC_CLASS_RO_$_TRITrishadowEvaluationRoot
- __OBJC_METACLASS_RO_$_TRIBmltDeploymentId
- __OBJC_METACLASS_RO_$_TRIClientBackgroundMLTask
- __OBJC_METACLASS_RO_$_TRIClientBmltCatalog
- __OBJC_METACLASS_RO_$_TRIShadowEvaluation
- __OBJC_METACLASS_RO_$_TRITrialBMLTFields
- __OBJC_METACLASS_RO_$_TRITriclientBackgroundMltaskRoot
- __OBJC_METACLASS_RO_$_TRITrishadowEvaluationRoot
- _descriptor.descriptor.21
- _descriptor.descriptor.47
- _descriptor.descriptor.58
- _descriptor.descriptor.83
- _descriptor.fields.22
- _descriptor.fields.48
- _descriptor.fields.59
- _descriptor.fields.84
- _objc_msgSend$bmltFields
- _objc_msgSend$setBmltFields:
- _objc_msgSend$setClientBmltFactorPackSetId:
- _objc_msgSend$setClientBmltId:
CStrings:
+ "MlruntimeEvaluation.pbobjc.m"
+ "TRIMlruntimeEvaluationRoot"
+ "_setError"
+ "getBytes:range:"
+ "hasError"
+ "setPosition:"
- "@\"TRITrialBMLTFields\""
- "T@\"NSString\",&,N,V_clientBmltFactorPackSetId"
- "T@\"NSString\",&,N,V_clientBmltId"
- "T@\"TRIClientBackgroundMLTask\",&,D,N"
- "T@\"TRIMLRuntimeEvaluation\",&,D,N"
- "T@\"TRIShadowEvaluation\",&,D,N"
- "T@\"TRITrialBMLTFields\",&,N,V_bmltFields"
- "TRIBmltDeploymentId"
- "TRIClientBackgroundMLTask"
- "TRIClientBmltCatalog"
- "TRIShadowEvaluation"
- "TRITrialBMLTFields"
- "TRITriclientBackgroundMltaskRoot"
- "TRITrishadowEvaluationRoot"
- "Ti,N,V_clientBmltTargetingRuleGroupOrdinal"
- "TriclientBackgroundMltask.pbobjc.m"
- "TrishadowEvaluation.pbobjc.m"
- "_bmltFields"
- "_clientBmltFactorPackSetId"
- "_clientBmltId"
- "_clientBmltTargetingRuleGroupOrdinal"
- "bmltDeploymentIdArray"
- "bmltDeploymentIdArray_Count"
- "bmltFields"
- "bmlt_fields"
- "clientBackgroundMlTask"
- "clientBmltFactorPackSetId"
- "clientBmltId"
- "clientBmltTargetingRuleGroupOrdinal"
- "client_bmlt_factor_pack_set_id"
- "client_bmlt_id"
- "client_bmlt_targeting_rule_group_ordinal"
- "customTargeting"
- "customTargetingKeysArray"
- "customTargetingKeysArray_Count"
- "ensureBMLTFields"
- "hasBmltFields"
- "hasClientBackgroundMlTask"
- "hasClientBmltFactorPackSetId"
- "hasClientBmltId"
- "hasClientBmltTargetingRuleGroupOrdinal"
- "hasCustomTargeting"
- "hasShadowEvaluation"
- "hasTaskId"
- "mlRuntime"
- "setBmltFields:"
- "setClientBmltFactorPackSetId:"
- "setClientBmltId:"
- "setClientBmltTargetingRuleGroupOrdinal:"
- "setHasClientBmltTargetingRuleGroupOrdinal:"
- "shadowEvaluation"
- "taskId"
- "typeOneOfCase"
- "{?=\"clientBmltTargetingRuleGroupOrdinal\"b1}"

```
