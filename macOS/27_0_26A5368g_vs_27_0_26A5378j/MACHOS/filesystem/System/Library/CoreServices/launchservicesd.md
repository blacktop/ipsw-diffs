## launchservicesd

> `/System/Library/CoreServices/launchservicesd`

```diff

-  __TEXT.__text: 0x5cbc0
-  __TEXT.__auth_stubs: 0x1900
+  __TEXT.__text: 0x5d4c8
+  __TEXT.__auth_stubs: 0x18f0
   __TEXT.__objc_stubs: 0x6a0
   __TEXT.__objc_methlist: 0x68
-  __TEXT.__const: 0x380
-  __TEXT.__cstring: 0x381a
-  __TEXT.__oslogstring: 0xb9ad
+  __TEXT.__const: 0x390
+  __TEXT.__cstring: 0x3885
+  __TEXT.__oslogstring: 0xbdf2
   __TEXT.__gcc_except_tab: 0x5f8
   __TEXT.__objc_methname: 0x3c6
   __TEXT.__objc_classname: 0x1f
   __TEXT.__objc_methtype: 0x3b
-  __TEXT.__unwind_info: 0x16f8
-  __DATA_CONST.__const: 0x4b88
-  __DATA_CONST.__cfstring: 0xd80
+  __TEXT.__unwind_info: 0x1718
+  __DATA_CONST.__const: 0x4bd0
+  __DATA_CONST.__cfstring: 0xe40
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xc90
-  __DATA_CONST.__got: 0x680
+  __DATA_CONST.__auth_got: 0xc88
+  __DATA_CONST.__got: 0x688
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x100
   __DATA.__objc_selrefs: 0x1b8

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1389
+  Functions: 1396
   Symbols:   648
-  CStrings:  1408
+  CStrings:  1428
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Symbols:
+ __kLSApplicationCanBeIgnoredForParentExitDetectionKey
- _xpc_dictionary_get_array
CStrings:
+ " (quitting)"
+ " asn:0x0-0x"
+ ", %@"
+ "- App %{public}@, ignoring acquired app %{public}@ — has kLSCanBeIgnoredForParentExitDetectionEntitlement."
+ "- App %{public}@, ignoring child app %{public}@ — has kLSCanBeIgnoredForParentExitDetectionEntitlement."
+ "AddOwnedApplication: app=%{public}@/%{private}@ refusing to acquire %{public}@/%{private}@ because it (or one of its ancestors) has kLSCanBeIgnoredForParentExitDetectionEntitlement."
+ "AddOwnedApplication: app=%{public}@/%{private}@, adding %{public}@/%{private}@ as an acquired app."
+ "AddOwnedApplication: app=%{public}@/%{private}@, called with NULL acquiredAppRef."
+ "AddOwnedApplication: app=%{public}@/%{private}@, refusing to add an acquired app to itself."
+ "App %{public}@ ignoring coalition pid=%{public}d — has kLSCanBeIgnoredForParentExitDetectionEntitlement."
+ "App %{public}@ ignoring related-coalition pid=%{public}d — has kLSCanBeIgnoredForParentExitDetectionEntitlement."
+ "Attempting to set the parent application of %{public}@/%{private}@ to an application %{public}@/%{private}@, which we are the parent of, which would be bad."
+ "Attempting to set the parent application of %{public}@/%{private}@ to itself, which would be bad."
+ "ClearCoalitions: app=%{public}@/%{private}@, clearing fCoalition=%{public}lld and %{public}zu related coalitions."
+ "DEATH: Removing from %{public}@/%{private}@ the owned application %{public}@/%{private}@"
+ "DEATH: Responsible application %{public}@/%{private}@ is still alive, so we're done."
+ "DEATH: Unregistering, parentApp %{public}@ still has children or coalition processes."
+ "LSApplication::CopyChildAndRelatedApplications(%{public}@/%{private}@) => %{public}@"
+ "LSApplication::CopyChildApplications(%{public}@/%{private}@) => %{public}@"
+ "RemoveOwnedApplication: app=%{public}@/%{private}@, removing ownership of app=%{public}@/%{private}@"
+ "SetApplicationOwner:app=%{public}@/%{private}@, setting owner to %{public}@/%{private}@ ( was %{public}@/%{private}@)"
+ "[ %@"
+ "[ ]"
+ "com.apple.private.launchservices.canBeIgnoredForParentExitDetection"
+ "com.apple.systemevents"
+ "enableQuitReally: %{BOOL}d, log version %d."
+ "inheritApplicationSubordinateResources: app=%{public}@/%{private}@ Adding related coalition id %{public}lld with %{public}zu pids inherited from %{public}@/%{private}@ to this app's related coalitions."
+ "inheritApplicationSubordinateResources: app=%{public}@/%{private}@ Not adding empty related application coalition id %{public}lld from %{public}@/%{private}@ to the related coalitions for this app."
+ "inheritApplicationSubordinateResources: app=%{public}@/%{private}@ moving related application %{public}@/%{private}@ to this application."
+ "inheritApplicationSubprocesses: app=%{public}@/%{private}@ Ignoring foreground child application %{public}@/%{private}@ ."
+ "inheritApplicationSubprocesses: app=%{public}@/%{private}@, inheriting resources from %{public}@ (%{public}@)/%{public}@"
- " asn:0x0-"
- "(quitting) "
- "AddAcquiredApplication(%{public}@/%{private}@), refusing to add an acquired app to itself."
- "AddAcquiredApplication(%{public}@/%{private}@, acquiredApp=%{public}@/%{private}@ childrenApps = %{public}@"
- "AddAcquiredApplication(), removing ourselves %{public}@/%{private}@ as a child app of %{public}@/%{private}@"
- "AddAcquiredApplication(), removing ourselves %{public}@/%{private}@ as a child app of %{public}@/%{private}@ because we are already responsible for it."
- "AddAcquiredApplication: app=%{public}@/%{private}@ Adding application coalition id %{public}lld from %{public}@/%{private}@ to the related coalitions for this app."
- "AddAcquiredApplication: app=%{public}@/%{private}@ Adding coalition id %{public}lld to the related coalitions from %{public}@/%{private}@ this process."
- "AddAcquiredApplication: app=%{public}@/%{private}@ moving related application %{public}@/%{private}@ to this application."
- "Adding application 0x0-0x%{public}llx/%{private}@ as a acquired app of %{public}@"
- "DEATH: Removing from %{public}@/%{private}@ the acquired application %{public}@/%{private}@"
- "DEATH: Unregistering, parentApp %{public}@ still has children or coalition procesess."
- "RESPONSIBLE: Clearing coalition and related coalition IDs from application because its owner is non-NULL, app=%{public}@/%{private}@"
- "RESPONSIBLE: Setting owner for app=%{public}@/%{private}@ to %{public}@/%{private}@"
- "enableQuitReally: %{BOOL}d"
- "inheritApplicationSubprocesses: app=%{public}@/%{private}@ Ignoring forgeround child application %{public}@/%{private}@ ."
- "inheritApplicationSubprocesses: app=%{public}@/%{private}@, inheriting resources from %{public}@/%{public}@"

```
