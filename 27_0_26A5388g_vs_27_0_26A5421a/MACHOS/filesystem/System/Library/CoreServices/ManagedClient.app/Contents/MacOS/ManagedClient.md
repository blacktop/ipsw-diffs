## ManagedClient

> `/System/Library/CoreServices/ManagedClient.app/Contents/MacOS/ManagedClient`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1841.0.0.0.0
-  __TEXT.__text: 0xbf550
+1842.1.1.0.0
+  __TEXT.__text: 0xbf490
   __TEXT.__auth_stubs: 0x2420
-  __TEXT.__objc_stubs: 0x75e0
-  __TEXT.__objc_methlist: 0x2364
+  __TEXT.__objc_stubs: 0x7600
+  __TEXT.__objc_methlist: 0x2374
   __TEXT.__const: 0x209
-  __TEXT.__gcc_except_tab: 0x2428
-  __TEXT.__cstring: 0x3bcf9
-  __TEXT.__oslogstring: 0x32153
+  __TEXT.__gcc_except_tab: 0x246c
+  __TEXT.__cstring: 0x3bb03
+  __TEXT.__oslogstring: 0x32165
   __TEXT.__objc_classname: 0x50f
   __TEXT.__objc_methtype: 0x19d2
-  __TEXT.__objc_methname: 0x7ec5
+  __TEXT.__objc_methname: 0x7ef1
   __TEXT.__unwind_info: 0x1be8
   __DATA_CONST.__const: 0x17c8
-  __DATA_CONST.__cfstring: 0xb4e0
+  __DATA_CONST.__cfstring: 0xb300
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x38

   __DATA_CONST.__got: 0x910
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x2418
-  __DATA.__objc_selrefs: 0x2330
+  __DATA.__objc_selrefs: 0x2338
   __DATA.__objc_ivar: 0x190
   __DATA.__objc_data: 0x780
   __DATA.__data: 0x2da

   - /usr/lib/libcups.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 3170
+  Functions: 3172
   Symbols:   877
-  CStrings:  6404
+  CStrings:  6392
 
CStrings:
+ "MCX.clearLaunchRestrictionsForUnmanagedComputer: computer is unmanaged, clearing App Launch Restrictions"
+ "Persistent store R/O provisioning read (cmd=%d) called by uid=%d"
+ "R/O provisioning-profile read denied for '%s' - missing entitlement"
+ "clearLaunchRestrictionsForUnmanagedComputer"
+ "mcxSvr_allprovisioningprofileswithfilter called by uid=%d"
+ "mcxSvr_allprovisioningprofileswithfilter denied for '%s' - missing entitlement"
- "MCX -postCompositeRestrictions restrictions defer minor days = %ld, major days = %ld, nonOS days = %ld, allowFastSecUpdates = %s, allowFastSecUpdatesRollback = %s "
- "MCX -postCompositeRestrictions restrictions forceDeferSU = %s; forceDeferAppSU = %s; forceDeferMajorSU = %s; defer days = %ld"
- "MCX -postCompositeRestrictions unable to save SU managed prefs out"
- "MajorOSManagedDeferredInstallDelay"
- "ManagedDeferredInstallDelay"
- "ManagedDisableSplat"
- "ManagedDisableSplatRollback"
- "MinorOSManagedDeferredInstallDelay"
- "NonOSManagedDeferredInstallDelay"
- "allowRapidSecurityResponseInstallation"
- "allowRapidSecurityResponseRemoval"
- "enforcedSoftwareUpdateDelay"
- "enforcedSoftwareUpdateMajorOSDeferredInstallDelay"
- "enforcedSoftwareUpdateMinorOSDeferredInstallDelay"
- "enforcedSoftwareUpdateNonOSDeferredInstallDelay"
- "forceDelayedAppSoftwareUpdates"
- "forceDelayedMajorSoftwareUpdates"
- "forceDelayedSoftwareUpdates"
```
