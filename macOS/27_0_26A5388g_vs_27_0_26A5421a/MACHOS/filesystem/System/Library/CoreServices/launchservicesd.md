## launchservicesd

> `/System/Library/CoreServices/launchservicesd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_classrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1510.400.0.0.0
-  __TEXT.__text: 0x5d69c
+1517.0.1.401.0
+  __TEXT.__text: 0x5eaac
   __TEXT.__auth_stubs: 0x1900
   __TEXT.__objc_stubs: 0x6a0
   __TEXT.__objc_methlist: 0x68
   __TEXT.__const: 0x390
-  __TEXT.__cstring: 0x3909
-  __TEXT.__oslogstring: 0xbe32
+  __TEXT.__cstring: 0x3989
+  __TEXT.__oslogstring: 0xc2fb
   __TEXT.__gcc_except_tab: 0x61c
   __TEXT.__objc_methname: 0x3c6
   __TEXT.__objc_classname: 0x1f
   __TEXT.__objc_methtype: 0x3b
-  __TEXT.__unwind_info: 0x1718
-  __DATA_CONST.__const: 0x4bd8
-  __DATA_CONST.__cfstring: 0xe60
+  __TEXT.__unwind_info: 0x1748
+  __DATA_CONST.__const: 0x4d60
+  __DATA_CONST.__cfstring: 0xea0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0xc90
-  __DATA_CONST.__got: 0x688
+  __DATA_CONST.__got: 0x6a8
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x100
   __DATA.__objc_selrefs: 0x1b8

   __DATA.__objc_data: 0x50
   __DATA.__data: 0x150
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x818
+  __DATA.__bss: 0x828
   __DATA.__common: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1397
-  Symbols:   649
-  CStrings:  1313
+  Functions: 1409
+  Symbols:   653
+  CStrings:  1331
 
Symbols:
+ __kLSApplicationDisclaimAsParentApplicationKey
+ __kLSApplicationDoNotTALRelaunchKey
+ __kLSApplicationHasReExecedItselfKey
+ __kLSApplicationPossibleForegroundOwnerApplicationsASNsArrayKey
+ __kLSLaunchedPersonaUIDKey
- __kLSApplicationHasAVisibleOwnerApplicationASNsArrayKey
CStrings:
+ "%@%@"
+ "%{public}s(app=%{public}@/%{private}@ atPosition=%{public}ld)"
+ "::HandleApplicationReExec(app=%{public}@/%{private}@)"
+ "::HandleApplicationReExec(app=%{public}@/%{private}@) had fetched its launch modifiers, so clearing them."
+ "::HandleApplicationReExec(app=%{public}@/%{private}@), adding bring-forward launch modifiers %{public}s"
+ "::HandleApplicationReExec(app=%{public}@/%{private}@), previous instance had signalled."
+ "::HandleApplicationReExec(app=%{public}@/%{private}@), previous instance was frontmost"
+ "::HandleApplicationReExec(app=%{public}@/%{private}@), previous instance was registered"
+ "::HandleApplicationReExec(app=%{public}@/%{private}@), refreshing entitlements."
+ "::HandleApplicationReExec(app=%{public}@/%{private}@), removing all inappropriate keys from app record."
+ "::HandleApplicationReExec(app=%{public}@/%{private}@), removing from visible process list"
+ "::HandleApplicationReExec(app=%{public}@/%{private}@), sending kLSNotificationApplicationReExeced notification"
+ "APP: Application %{public}@ has a different audit_token, %d/%d vs %d/%d, so probably re-execed."
+ "Adding %{public}@/%{private}@ to visible list at offset %{public}ld"
+ "Adding %{public}@/%{private}@ to visible list end of list"
+ "AppPIDToSession, EVENT-HANDLER Received notification that pid %{public}d exec-ed, after registering, associatedApp=%{private}@, source=%{public}p"
+ "AppPIDToSession, EVENT-HANDLER Received notification that pid %{public}d exec-ed, associatedApp=%{private}@, source=%{public}p"
+ "B16@?0^{__CFDictionary=}8"
+ "[["
+ "]]"
+ "applicationCheckIn(%{public}@/%{private}@), birth after a pre-hint."
+ "applicationCheckIn(%{public}@/%{private}@), birth but not pre-hinted."
+ "applicationCheckIn(%{public}@/%{private}@), rebirth."
+ "com.apple.private.launchservices.disclaimroleasparentapplication"
+ "kLSNotificationApplicationReExeced"
+ "kLSNotifyApplicationRebirth"
- ", %@"
- "APP: Application %{public}@ has a different audit_token, %d/%d vs %d/%d, so reverting any previous checkin."
- "Adding %{public}s to end of visible list."
- "AppPIDToSession, EVENT-HANDLER Received notification that pid %{public}d exec-ed, associatedApp=%{private}@, so if it has checked in as an application things are going to be weird, source=%{public}p"
- "[ %@"
- "[ ]"
- "application=%{public}@, checkEntitlement(%@) failed because the audit token is unset."
- "com.apple.systemevents"
```
