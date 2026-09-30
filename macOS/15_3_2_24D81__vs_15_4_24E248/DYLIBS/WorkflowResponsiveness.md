## WorkflowResponsiveness

> `/System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/Versions/A/WorkflowResponsiveness`

```diff

-383.2.0.0.0
-  __TEXT.__text: 0x2a4a0
+383.5.0.0.0
+  __TEXT.__text: 0x2a284
   __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_methlist: 0x754
+  __TEXT.__objc_methlist: 0x790
   __TEXT.__const: 0xf0
-  __TEXT.__gcc_except_tab: 0xbe4
+  __TEXT.__gcc_except_tab: 0xbac
   __TEXT.__cstring: 0x1fd1
   __TEXT.__oslogstring: 0x4014
-  __TEXT.__unwind_info: 0x5a0
+  __TEXT.__unwind_info: 0x5b0
   __TEXT.__objc_classname: 0x11a
   __TEXT.__objc_methname: 0x241c
   __TEXT.__objc_methtype: 0x26a

   __AUTH_CONST.__auth_got: 0x2d8
   __AUTH_CONST.__const: 0x5e0
   __AUTH_CONST.__cfstring: 0x1f80
-  __AUTH_CONST.__objc_const: 0x1690
+  __AUTH_CONST.__objc_const: 0x1638
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0x370

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 9066CA42-FBE0-31BC-B6AF-3B396A119AB2
-  Functions: 501
-  Symbols:   1207
+  UUID: 018E03A9-DA95-320E-8E87-4435382D51F7
+  Functions: 591
+  Symbols:   1294
   CStrings:  1218
 
Symbols:
+ +[WRWorkflowEventTracker makeTailspinDirectory].cold.1
+ +[WRWorkflowEventTracker tailspinDirectory].cold.1
+ -[WRSignpostTracker initWithEncodedDict:signpost:error:].cold.1
+ -[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:checkForOverrides:error:].cold.10
+ -[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:checkForOverrides:error:].cold.8
+ -[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:checkForOverrides:error:].cold.9
+ -[WRWorkflowEventTracker doneHandlingSignpostsWithEndTimeMachContNs:].cold.1
+ -[WRWorkflowEventTracker generateTelemetry].cold.5
+ -[WRWorkflowEventTracker generateTelemetry].cold.6
+ -[WRWorkflowEventTracker handleSignpost:].cold.10
+ -[WRWorkflowEventTracker handleSignpost:].cold.11
+ -[WRWorkflowEventTracker handleSignpost:].cold.9
+ -[WRWorkflowEventTracker handleSignpost:wrsignpost:].cold.5
+ -[WRWorkflowEventTracker handleSignpost:wrsignpost:].cold.6
+ -[WRWorkflowEventTracker handleSignpost:wrsignpost:].cold.7
+ -[WRWorkflowEventTracker initWithEncodedDict:error:].cold.1
+ -[WRWorkflowEventTracker initWithEncodedDict:error:].cold.2
+ -[WRWorkflowProviderAllWorkflows handleSettingsChanged:].cold.2
+ AllDiagnosticKeys.cold.1
+ AllSignpostKeys.cold.1
+ AllWorkflowKeys.cold.1
+ GCC_except_table140
+ GCC_except_table194
+ GCC_except_table234
+ GCC_except_table235
+ WRIsAppleInternal.cold.1
+ WRMachTimeFromNanosecondsUsingLiveTimebase.cold.1
+ WRSanitizeForCA.cold.1
+ _OUTLINED_FUNCTION_100
+ _OUTLINED_FUNCTION_101
+ _OUTLINED_FUNCTION_102
+ _OUTLINED_FUNCTION_103
+ _OUTLINED_FUNCTION_104
+ _OUTLINED_FUNCTION_105
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_49
+ _OUTLINED_FUNCTION_50
+ _OUTLINED_FUNCTION_51
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_58
+ _OUTLINED_FUNCTION_59
+ _OUTLINED_FUNCTION_60
+ _OUTLINED_FUNCTION_61
+ _OUTLINED_FUNCTION_62
+ _OUTLINED_FUNCTION_63
+ _OUTLINED_FUNCTION_64
+ _OUTLINED_FUNCTION_65
+ _OUTLINED_FUNCTION_66
+ _OUTLINED_FUNCTION_67
+ _OUTLINED_FUNCTION_68
+ _OUTLINED_FUNCTION_69
+ _OUTLINED_FUNCTION_70
+ _OUTLINED_FUNCTION_71
+ _OUTLINED_FUNCTION_72
+ _OUTLINED_FUNCTION_73
+ _OUTLINED_FUNCTION_74
+ _OUTLINED_FUNCTION_75
+ _OUTLINED_FUNCTION_76
+ _OUTLINED_FUNCTION_77
+ _OUTLINED_FUNCTION_78
+ _OUTLINED_FUNCTION_79
+ _OUTLINED_FUNCTION_80
+ _OUTLINED_FUNCTION_81
+ _OUTLINED_FUNCTION_82
+ _OUTLINED_FUNCTION_83
+ _OUTLINED_FUNCTION_84
+ _OUTLINED_FUNCTION_85
+ _OUTLINED_FUNCTION_86
+ _OUTLINED_FUNCTION_87
+ _OUTLINED_FUNCTION_88
+ _OUTLINED_FUNCTION_89
+ _OUTLINED_FUNCTION_90
+ _OUTLINED_FUNCTION_91
+ _OUTLINED_FUNCTION_92
+ _OUTLINED_FUNCTION_93
+ _OUTLINED_FUNCTION_94
+ _OUTLINED_FUNCTION_95
+ _OUTLINED_FUNCTION_96
+ _OUTLINED_FUNCTION_97
+ _OUTLINED_FUNCTION_98
+ _OUTLINED_FUNCTION_99
+ _TSPDumpOptions_EndTimestamp
+ _WRMachTimeFromNanosecondsUsingLiveTimebase
+ _WRValidateU64
+ __52-[WRWorkflowEventTracker handleSignpost:wrsignpost:]_block_invoke.cold.1
+ __58-[WRWorkflowEventTracker applySignpost:toSignpostTracker:]_block_invoke.cold.1
+ __MergedGlobals
+ _wrlog.cold.1
- -[WRWorkflowEventTracker applySignpost:toSignpostTracker:].cold.1
- -[WRWorkflowEventTracker applySignpost:toSignpostTracker:].cold.2
- -[WRWorkflowEventTracker applySignpost:toSignpostTracker:].cold.3
- -[WRWorkflowEventTracker applySignpost:toSignpostTracker:].cold.4
- -[WRWorkflowEventTracker encodedDict].cold.1
- -[WRWorkflowEventTracker encodedDict].cold.2
- -[WRWorkflowEventTracker eventIdentifierForSignpostObject:wrSignopst:].cold.1
- -[WRWorkflowEventTracker eventIdentifierForSignpostObject:wrSignopst:].cold.2
- -[WRWorkflowEventTracker gatherDiagnosticsWithTailspin:tailspinIncludeOSLogs:].cold.1
- -[WRWorkflowEventTracker gatherDiagnosticsWithTailspin:tailspinIncludeOSLogs:].cold.10
- -[WRWorkflowEventTracker gatherDiagnosticsWithTailspin:tailspinIncludeOSLogs:].cold.2
- -[WRWorkflowEventTracker gatherDiagnosticsWithTailspin:tailspinIncludeOSLogs:].cold.3
- -[WRWorkflowEventTracker gatherDiagnosticsWithTailspin:tailspinIncludeOSLogs:].cold.4
- -[WRWorkflowEventTracker gatherDiagnosticsWithTailspin:tailspinIncludeOSLogs:].cold.5
- -[WRWorkflowEventTracker gatherDiagnosticsWithTailspin:tailspinIncludeOSLogs:].cold.6
- -[WRWorkflowEventTracker gatherDiagnosticsWithTailspin:tailspinIncludeOSLogs:].cold.7
- -[WRWorkflowEventTracker gatherDiagnosticsWithTailspin:tailspinIncludeOSLogs:].cold.8
- -[WRWorkflowEventTracker gatherDiagnosticsWithTailspin:tailspinIncludeOSLogs:].cold.9
- -[WRWorkflowEventTracker reportErrorsAndResetAtMachContNs:date:].cold.1
- -[WRWorkflowEventTracker reportErrorsAndResetAtMachContNs:date:].cold.2
- -[WRWorkflowProviderSingleWorkflow handleSettingsChanged:].cold.1
- GCC_except_table139
- GCC_except_table192
- GCC_except_table236
- GCC_except_table237
- WRStringForDate.dateFormatter
- WRStringForDate.onceToken

```
