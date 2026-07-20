## libLaunchServicesSupport.dylib

> `/usr/lib/libLaunchServicesSupport.dylib`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-1507.0.0.0.0
-  __TEXT.__text: 0x1dea8
-  __TEXT.__auth_stubs: 0xc50
-  __TEXT.__objc_stubs: 0xec0
-  __TEXT.__objc_methlist: 0x3f4
-  __TEXT.__const: 0x140
-  __TEXT.__cstring: 0xbb0
-  __TEXT.__oslogstring: 0x5443
-  __TEXT.__gcc_except_tab: 0x2afc
-  __TEXT.__objc_methname: 0xd9c
-  __TEXT.__objc_classname: 0x3d
-  __TEXT.__objc_methtype: 0x1ff
-  __TEXT.__unwind_info: 0xa70
-  __DATA_CONST.__const: 0xe88
-  __DATA_CONST.__cfstring: 0xc80
-  __DATA_CONST.__objc_classlist: 0x10
+1510.400.0.0.0
+  __TEXT.__text: 0x1fea0
+  __TEXT.__auth_stubs: 0xc70
+  __TEXT.__objc_stubs: 0xf00
+  __TEXT.__objc_methlist: 0x454
+  __TEXT.__const: 0x150
+  __TEXT.__cstring: 0xc08
+  __TEXT.__oslogstring: 0x5be2
+  __TEXT.__gcc_except_tab: 0x2e7c
+  __TEXT.__objc_methname: 0xdcc
+  __TEXT.__objc_classname: 0x44
+  __TEXT.__objc_methtype: 0x220
+  __TEXT.__unwind_info: 0xb48
+  __DATA_CONST.__const: 0xee8
+  __DATA_CONST.__cfstring: 0xda0
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x498
-  __DATA_CONST.__auth_got: 0x638
+  __DATA_CONST.__objc_selrefs: 0x4a8
+  __DATA_CONST.__auth_got: 0x648
   __DATA_CONST.__got: 0x220
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0x548
-  __DATA.__objc_classrefs: 0x90
-  __DATA.__objc_superrefs: 0x8
-  __DATA.__objc_ivar: 0x3c
-  __DATA.__objc_data: 0xa0
+  __DATA.__objc_const: 0x618
+  __DATA.__objc_classrefs: 0x98
+  __DATA.__objc_superrefs: 0x10
+  __DATA.__objc_ivar: 0x40
+  __DATA.__objc_data: 0xf0
   __DATA.__data: 0xe8
   __DATA.__bss: 0x230
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libquit.dylib
-  Functions: 423
-  Symbols:   1111
-  CStrings:  600
+  Functions: 449
+  Symbols:   1169
+  CStrings:  629
 
Symbols:
+ +[_LSASN newWithASNRef:]
+ -[_LSASN asnRef]
+ -[_LSASN dealloc]
+ -[_LSASN description]
+ -[_LSASN initWithASNRef:]
+ -[_LSASN setAsnRef:]
+ GCC_except_table138
+ GCC_except_table146
+ GCC_except_table157
+ GCC_except_table161
+ GCC_except_table165
+ GCC_except_table173
+ GCC_except_table175
+ GCC_except_table176
+ GCC_except_table177
+ GCC_except_table178
+ GCC_except_table180
+ GCC_except_table181
+ GCC_except_table182
+ GCC_except_table183
+ GCC_except_table184
+ GCC_except_table185
+ GCC_except_table186
+ GCC_except_table20
+ GCC_except_table25
+ GCC_except_table26
+ GCC_except_table31
+ GCC_except_table56
+ GCC_except_table61
+ GCC_except_table63
+ GCC_except_table70
+ OBJC_IVAR_$__LSASN._asnRef
+ _CFStringCreateWithCString
+ _OBJC_CLASS_$__LSASN
+ _OBJC_METACLASS_$__LSASN
+ __LSIsApplicationRunningOrExited
+ __OBJC_$_CLASS_METHODS__LSASN
+ __OBJC_$_INSTANCE_METHODS__LSASN
+ __OBJC_$_INSTANCE_VARIABLES__LSASN
+ __OBJC_$_PROP_LIST__LSASN
+ __OBJC_CLASS_RO_$__LSASN
+ __OBJC_METACLASS_RO_$__LSASN
+ __Z19applicationIsExitedPK7__LSASN
+ __Z19namedPIDArrayStringPK9__CFArray
+ __Z28applicationIsRunningOrExitedPK7__LSASN
+ __ZL13appDictionaryPK7__LSASNi
+ __ZL14appsDictionaryPK9__CFArrayi
+ __ZL14pidDescriptionii
+ __ZL15pidDescriptionsPK9__CFArrayii
+ __ZL44scheduleCheckApplicationForExitedApplicationP13LSApplication
+ __ZL60terminateApplicationIfNonVisibleAndItsATypeWeCanAutomatiallyP6_LSASNP13LSApplication
+ __ZL61terminateAppropriateSubprocessesWhenEnclosingApplicationExitsP13LSApplication
+ ___ZL44scheduleCheckApplicationForExitedApplicationP13LSApplication_block_invoke
+ ___ZL60terminateApplicationIfNonVisibleAndItsATypeWeCanAutomatiallyP6_LSASNP13LSApplication_block_invoke
+ ___ZL60terminateApplicationIfNonVisibleAndItsATypeWeCanAutomatiallyP6_LSASNP13LSApplication_block_invoke_2
+ ___ZL61terminateAppropriateSubprocessesWhenEnclosingApplicationExitsP13LSApplication_block_invoke
+ ____Z19namedPIDArrayStringPK9__CFArray_block_invoke
+ ____ZL13appDictionaryPK7__LSASNi_block_invoke
+ ____ZL13appDictionaryPK7__LSASNi_block_invoke_2
+ ____ZL14appsDictionaryPK9__CFArrayi_block_invoke
+ ____ZL15pidDescriptionsPK9__CFArrayii_block_invoke
+ ____ZL44scheduleCheckApplicationForExitedApplicationP13LSApplication_block_invoke
+ ____ZL60terminateApplicationIfNonVisibleAndItsATypeWeCanAutomatiallyP6_LSASNP13LSApplication_block_invoke
+ ____ZL60terminateApplicationIfNonVisibleAndItsATypeWeCanAutomatiallyP6_LSASNP13LSApplication_block_invoke_2
+ ____ZL61terminateAppropriateSubprocessesWhenEnclosingApplicationExitsP13LSApplication_block_invoke
+ ___block_descriptor_44_ea8_32s_e18_B16?0^{__LSASN=}8l
+ ___block_descriptor_48_ea8_32s40c30_ZTS10CFReleaserIPK9__CFArrayE_e25_v32?0"NSNumber"8Q16^B24l
+ ___block_descriptor_48_ea8_32s40s_e18_B16?0^{__LSASN=}8l
+ ___block_descriptor_48_ea8_32s40s_e5_v8?0l
+ ___copy_helper_block_ea8_32s40c30_ZTS10CFReleaserIPK9__CFArrayE
+ ___destroy_helper_block_ea8_32s40c30_ZTS10CFReleaserIPK9__CFArrayE
+ _copyProcessNameString
+ _objc_msgSend$isKindOfClass:
+ _objc_msgSend$newWithASNRef:
+ _processNameString
- GCC_except_table139
- GCC_except_table148
- GCC_except_table162
- GCC_except_table169
- GCC_except_table22
- GCC_except_table32
- GCC_except_table37
- GCC_except_table49
- __ZL13appDictionaryPK7__LSASNb
- ___ZL13appDictionaryPK7__LSASNb_block_invoke
- ___ZL44scheduleCheckApplicationForExitedApplicationP13LSApplicationd_block_invoke
- ____ZL13appDictionaryPK7__LSASNb_block_invoke
- ____ZL13appDictionaryPK7__LSASNb_block_invoke_2
- ____ZL13appDictionaryPK7__LSASNb_block_invoke_3
- ____ZL27registerSysdiagonoseHandlerP12NSDictionaryIP8NSStringP8NSObjectEPU15__autoreleasingP7NSError_block_invoke_4
- ___block_descriptor_41_ea8_32s_e18_B16?0^{__LSASN=}8l
- ___block_descriptor_44_ea8_32s_e21_B16?0^{__CFNumber=}8l
CStrings:
+ "%d"
+ "%d/%@"
+ "ParentASN"
+ "QUITSUPPORT: Listening for kLSNotifyApplicationReady to track all application checkins."
+ "T^{__LSASN=},V_asnRef"
+ "[ %@ ]"
+ "^{__LSASN=}"
+ "_LSASN"
+ "_LSForceQuitApplication: Coalition pid %{public}d/%{public}@ in coalition should be handled as an application, app=%{public}@."
+ "_LSForceQuitApplication: Skipping pid %{public}d/%{public}@ in coalition because it is a foreground application, app=%{public}@."
+ "_LSForceQuitApplication: Skipping pid %{public}d/%{public}@ in coalition because it is a uielement application with a visible attribute, app=%{public}@."
+ "_LSForceQuitApplication: Skipping pid %{public}d/%{public}@ in coalition because it matches the application being killed, %{public}@."
+ "_LSForceQuitApplication: asn=%{public}@ blocking waiting for LQReportHang for pid %{public}d/%{public}@ to complete."
+ "_LSForceQuitApplication: asn=%{public}@ calling LQReportHang for pid=%{public}d/%{public}@"
+ "_LSForceQuitApplication: asn=%{public}@ cancellation handler for the death of main application pid %{public}d/%{public}@."
+ "_LSForceQuitApplication: asn=%{public}@ cancelling dispatch source after completion about the death of main application pid %{public}d/%{public}@."
+ "_LSForceQuitApplication: asn=%{public}@ failed attempting to kill main application pid %{public}d/%{public}@ with error %{public}@."
+ "_LSForceQuitApplication: asn=%{public}@ killing with SIGTERM main application pid %{public}d/%{public}@."
+ "_LSForceQuitApplication: asn=%{public}@ notified about the death of main application pid %{public}d/%{public}@."
+ "_LSForceQuitApplication: asn=%{public}@ pid=%{public}d/%{public}@, is no longer running so skipping the kill()."
+ "_LSForceQuitApplication: asn=%{public}@, finished LQReportHang for pid=%{public}d/%{public}@"
+ "_LSForceQuitApplication: asn=%{public}@, timeout waiting for SIGTERM so sending SIGKILL on main application pid %{public}d/%{public}@."
+ "applicationDeath: app=%{public}@, checking for subprocesses which should be automatically terminated."
+ "applicationStillHasRunningCoalitionOrRelatedCoalitionProcesses: app=%{public}@ child coalition pid %{public}d/%{public}@ is a job managed by launchd so this app does not yet have lingering subprocesses, job=%{public}@"
+ "applicationStillHasRunningCoalitionOrRelatedCoalitionProcesses: app=%{public}@ child coalition pid %{public}d/%{public}@ is non-foreground, non-job process so app still has lingering subprocesses."
+ "applicationStillHasRunningCoalitionOrRelatedCoalitionProcesses: app=%{public}@ related coalition pid %{public}d/%{public}@ is a job but not managed by launchd so this application has a lingering subprocess, job=%{public}@."
+ "applicationStillHasRunningCoalitionOrRelatedCoalitionProcesses: app=%{public}@ related coalitions pid %{public}d/%{public}@ is a foreground app so this app does not yet have lingering subprocesses."
+ "applicationStillHasRunningCoalitionOrRelatedCoalitionProcesses: app=%{public}@ related coalitions pid %{public}d/%{public}@ is an app which is not user-visible, so need to check if it's an allowed job."
+ "applicationStillHasRunningCoalitionOrRelatedCoalitionProcesses: app=%{public}@ related coalitions pid %{public}d/%{public}@ is an app which is user-visible so this app does not yet have lingering subprocesses."
+ "childASNs"
+ "depth"
+ "enableQuitTrackingSupport: %{BOOL}d, log version %d."
+ "informBTM: Informing BTM about an application running without visible UI, app=%{public}@ url=%{private}@ continueTracking=%{BOOL}d"
+ "killPID: pid=%{public}d/%{public}@ has already exited, ignoring"
+ "launchJobCheck: app=%{public}@ hostPid=%{public}d/%{public}@ job=%{public}@ PID domain job allowed by quit."
+ "launchJobCheck: app=%{public}@ hostPid=%{public}d/%{public}@ job=%{public}@ allowed by exception."
+ "newWithASNRef:"
+ "nonVisibleChildrenASNs"
+ "nonVisibleChildrenApps"
+ "schedule: app=%{public}@ cheking in %{public}g seconds to confirm it has completed exiting."
+ "setAsnRef:"
+ "terminateAppIf: Failed to force quit or kill application %{public}@, error=%{public}@"
+ "terminateAppIf: app=%{public}@ is a subordinate ui-element of %{public}@ with user visiblity, so not a subprocess automatically terminated."
+ "terminateAppIf: app=%{public}@ is foreground so not a subprocess type we would terminate automatically."
+ "terminateAppIf: app=%{public}@ supported subordinate termination, so terminating all remaining subordinate processes now."
+ "terminateAppIf: app=%{public}@ supports automatic termination, so terminating all subordinate processes in %{public}g seconds."
+ "terminateAppIf: app=%{public}@ supports subordinate termination, so terminating all subordinate processes in %{public}g seconds."
+ "terminateAppIf: app=%{public}@ supports sudden termination, so terminating all subordinate processes in %{public}g seconds."
+ "terminateAppIf: app=%{public}@, successfully force quit application"
+ "terminateAppIf: app=%{public}@, successfully quit or killed application"
+ "terminateAppropriateSubprocesess: app=%{public}@, checking children and related applications for non-visbile terminatable apps %{public}@."
+ "terminateAppropriateSubprocesess: app=%{public}@, checking for coalition pids for non-visible terminatable apps %{public}@."
+ "terminateAppropriateSubprocesess: app=%{public}@, coalition pid %{public}d matches related app which has already been handled."
+ "terminateAppropriateSubprocesess: app=%{public}@, coalition pid %{public}d matches the responsible app so skipping."
+ "terminateAppropriateSubprocesess: app=%{public}@, related app matches the responsible app so skipping."
+ "v24@0:8^{__LSASN=}16"
- "QUITREALLY: Listening for kLSNotifyApplicationReady to track all application checkins."
- "_LSForceQuitApplication: Coalition pid %{public}d in coalition should be handled as an application, app=%{public}@."
- "_LSForceQuitApplication: Skipping pid %{public}d in coalition because it is a foreground application, app=%{public}@."
- "_LSForceQuitApplication: Skipping pid %{public}d in coalition because it is a uielement application with a visible attribute, app=%{public}@."
- "_LSForceQuitApplication: Skipping pid %{public}d in coalition because it matches the application being killed, %{public}@."
- "_LSForceQuitApplication: asn=%{public}@ blocking waiting for LQReportHang for pid %{public}d to complete."
- "_LSForceQuitApplication: asn=%{public}@ calling LQReportHang for pid=%{public}d"
- "_LSForceQuitApplication: asn=%{public}@ cancellation handler for the death of main application pid %{public}d."
- "_LSForceQuitApplication: asn=%{public}@ cancelling dispatch source after completion about the death of main application pid %{public}d."
- "_LSForceQuitApplication: asn=%{public}@ failed attempting to kill main application pid %{public}d with error %{public}@."
- "_LSForceQuitApplication: asn=%{public}@ killing with SIGTERM main application pid %{public}d."
- "_LSForceQuitApplication: asn=%{public}@ notified about the death of main application pid %{public}d."
- "_LSForceQuitApplication: asn=%{public}@ pid=%{public}d, is no longer running so skipping the kill()."
- "_LSForceQuitApplication: asn=%{public}@, finished LQReportHang for pid=%{public}d"
- "_LSForceQuitApplication: asn=%{public}@, timeout waiting for SIGTERM so sending SIGKILL on main application pid %{public}d."
- "application: app=%{public}@ finished exiting before we processed the death notification, so no need to track it."
- "applicationStillHasRunningCoalitionOrRelatedCoalitionProcesses: app=%{public}@ child coalition pid %{public}d is a job managed by launchd so this app does not yet have lingering subprocesses, job=%{public}@"
- "applicationStillHasRunningCoalitionOrRelatedCoalitionProcesses: app=%{public}@ child coalition pid %{public}d is non-foreground, non-job process so app still has lingering subprocesses."
- "applicationStillHasRunningCoalitionOrRelatedCoalitionProcesses: app=%{public}@ related coalition pid %{public}d is a job but not managed by launchd so this application has a lingering subprocess, job=%{public}@."
- "applicationStillHasRunningCoalitionOrRelatedCoalitionProcesses: app=%{public}@ related coalitions pid %{public}d is a foreground app so this app does not yet have lingering subprocesses."
- "applicationStillHasRunningCoalitionOrRelatedCoalitionProcesses: app=%{public}@ related coalitions pid %{public}d is an app which is not user-visible, so need to check if it's an allowed job."
- "applicationStillHasRunningCoalitionOrRelatedCoalitionProcesses: app=%{public}@ related coalitions pid %{public}d is an app which is user-visible so this app does not yet have lingering subprocesses."
- "enableQuitReally: %{BOOL}d, log version %d."
- "informBTM: Informing BTM about an application running without visible UI, app=%{public}@ url=%{private}@"
- "killPID: pid=%{public}d has already exited, ignoring"
- "launchJobCheck: app=%{public}@ hostPid=%{public}d job=%{public}@ PID domain job allowed by quit."
- "launchJobCheck: app=%{public}@ hostPid=%{public}d job=%{public}@ allowed by exception."
```
