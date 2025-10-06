## installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

-781.0.0.0.1
-  __TEXT.__text: 0xa7ab4
-  __TEXT.__auth_stubs: 0x1130
-  __TEXT.__objc_stubs: 0xb0a0
-  __TEXT.__objc_methlist: 0x5e04
+784.40.1.0.0
+  __TEXT.__text: 0xa74a4
+  __TEXT.__auth_stubs: 0x1160
+  __TEXT.__objc_stubs: 0xaee0
+  __TEXT.__objc_methlist: 0x5d74
   __TEXT.__const: 0x210
-  __TEXT.__cstring: 0x18fb1
-  __TEXT.__objc_methname: 0x110c1
-  __TEXT.__objc_classname: 0xa21
-  __TEXT.__objc_methtype: 0x23e5
-  __TEXT.__oslogstring: 0xe083
+  __TEXT.__cstring: 0x18f5c
+  __TEXT.__objc_methname: 0x10e8a
+  __TEXT.__objc_classname: 0xa1d
+  __TEXT.__objc_methtype: 0x23e4
+  __TEXT.__oslogstring: 0xe02b
   __TEXT.__gcc_except_tab: 0x32fc
   __TEXT.__ustring: 0x1a68
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x26f8
-  __DATA_CONST.__auth_got: 0x8a8
+  __TEXT.__unwind_info: 0x26d0
+  __DATA_CONST.__auth_got: 0x8c0
   __DATA_CONST.__got: 0x458
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2d60
+  __DATA_CONST.__const: 0x2d40
   __DATA_CONST.__cfstring: 0x9dc0
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xc580
-  __DATA.__objc_selrefs: 0x3420
-  __DATA.__objc_ivar: 0x4b4
+  __DATA.__objc_const: 0xc4c0
+  __DATA.__objc_selrefs: 0x33a8
+  __DATA.__objc_ivar: 0x4a4
   __DATA.__objc_data: 0x1720
   __DATA.__data: 0x6b0
   __DATA.__crash_info: 0x148

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CAE4C5A0-52DF-3914-BF97-06376132231F
-  Functions: 3375
-  Symbols:   429
-  CStrings:  6863
+  UUID: 99C58EDA-E903-34D2-AF80-FF7E61407593
+  Functions: 3360
+  Symbols:   432
+  CStrings:  6838
 
Symbols:
+ _MobileInstallationReconcileContentsOnKnownOSModules
+ _MobileInstallationRegisterContentsOnOSModuleAtURL
+ _MobileInstallationUnregisterContentsOnOSModuleAtURL
CStrings:
+ "%s: Reconciling known OSModule URLs %@ set by client %@"
+ "%s: Registering contents for OSModule at %@ by client %@"
+ "%s: Unregistering contents of OSModule at %@ by client %@"
+ "-[IXSCoordinatedAppInstall scheduledAppUpdateReadyToExecute]"
+ "-[IXTerminationAssertion _terminationAssertionForBundleIDs:description:terminationResistance:error:]"
+ "-[IXTerminationAssertion acquireAssertion:]"
+ "-[IXTerminationAssertion assertionTargetProcessDidExit:]"
+ "-[IXTerminationAssertion initForBundleIDs:description:terminationResistance:error:]"
+ "-[IXTerminationAssertion setTermAssertion:]"
+ "21:51:38"
+ "@\"IXTerminationAssertion\""
+ "IXTerminationAssertion"
+ "Sep 28 2025"
+ "T@\"IXTerminationAssertion\",&,N,V_terminationAssertion"
+ "scheduledAppUpdateReadyToExecute"
- "%s: Failed to schedule install task %@ : %@. Executing it right away."
- "%s: STUB: Reconciling known OSModule URLs %@ set by client %@"
- "%s: STUB: Registering contents for OSModule at %@ by client %@"
- "%s: STUB: Unregistering contents of OSModule at %@ by client %@"
- "-[IXSAppUpdateScheduler _scheduleNextTask]_block_invoke"
- "-[IXSCoordinatedAppInstall scheduledAppUpdateReadyToExecuteAndRunBlockWhenComplete:]"
- "-[IXSTerminationAssertion _terminationAssertionForBundleIDs:description:terminationResistance:error:]"
- "-[IXSTerminationAssertion acquireAssertion:]"
- "-[IXSTerminationAssertion assertionTargetProcessDidExit:]"
- "-[IXSTerminationAssertion initForBundleIDs:description:terminationResistance:error:]"
- "-[IXSTerminationAssertion setTermAssertion:]"
- "23:12:56"
- "@\"IXSTerminationAssertion\""
- "IXSTerminationAssertion"
- "Sep 16 2025"
- "T@\"IXSTerminationAssertion\",&,N,V_terminationAssertion"
- "T@\"NSArray\",&,N,V_queuedInstalls"
- "T@?,C,N,V_schedulerCallback"
- "TB,N,V_scheduledInstallIsRunning"
- "TQ,N,V_scheduledInstallCount"
- "_onQueue_dequeueInstallTask"
- "_onQueue_enqueueInstallTask:"
- "_onQueue_removeEnqueuedTask:"
- "_queuedInstalls"
- "_scheduleNextTask"
- "_scheduledInstallCount"
- "_scheduledInstallIsRunning"
- "_schedulerCallback"
- "lastObject"
- "queuedInstalls"
- "removeLastObject"
- "scheduledAppUpdateReadyToExecuteAndRunBlockWhenComplete:"
- "scheduledInstallCount"
- "scheduledInstallIsRunning"
- "scheduledUpdateComplete"
- "schedulerCallback"
- "setQueuedInstalls:"
- "setScheduledInstallCount:"
- "setScheduledInstallIsRunning:"
- "setSchedulerCallback:"

```
