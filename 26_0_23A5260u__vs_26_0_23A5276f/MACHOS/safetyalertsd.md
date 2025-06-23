## safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

-64.0.18.0.0
-  __TEXT.__text: 0xd0dac
-  __TEXT.__auth_stubs: 0xfc0
+64.0.19.0.0
+  __TEXT.__text: 0xd11b8
+  __TEXT.__auth_stubs: 0xfd0
   __TEXT.__objc_stubs: 0x2de0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xa84
   __TEXT.__const: 0x9b8c
-  __TEXT.__gcc_except_tab: 0xc59c
-  __TEXT.__cstring: 0x519a
-  __TEXT.__oslogstring: 0x33c5a
+  __TEXT.__gcc_except_tab: 0xc5b4
+  __TEXT.__cstring: 0x51db
+  __TEXT.__oslogstring: 0x33c59
   __TEXT.__objc_classname: 0x1ea
   __TEXT.__objc_methname: 0x36bd
   __TEXT.__objc_methtype: 0x1936
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x3bf8
-  __DATA_CONST.__auth_got: 0x7f0
+  __TEXT.__unwind_info: 0x3bc8
+  __DATA_CONST.__auth_got: 0x7f8
   __DATA_CONST.__got: 0x4e8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x7f28
-  __DATA_CONST.__cfstring: 0x5760
+  __DATA_CONST.__const: 0x7f08
+  __DATA_CONST.__cfstring: 0x57c0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_ivar: 0x7c
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x430
-  __DATA.__bss: 0x5c8
+  __DATA.__bss: 0x5f0
   __DATA.__common: 0x48
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7F519A1E-B69D-3E43-869D-7AB0436D4DED
+  UUID: A76E251C-F9D2-391A-8B26-E96801DBD078
   Functions: 3191
-  Symbols:   427
-  CStrings:  4370
+  Symbols:   428
+  CStrings:  4374
 
Symbols:
+ _objc_release_x9
CStrings:
+ "ENVIRONMENT_IDENTIFIER"
+ "cacheFetchDitherSeconds"
+ "def"
+ "environmentId"
+ "{\"msg%{public}.0s\":\"#igv,validate,not internal install\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,schedulePreCacheAfterTime\", \"ditheredStartTime\":\"%{public}.2f\", \"maxDitheredStartTime\":\"%{public}.2f\"}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,save,dispatched\", \"debugName\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#uimetrics,SAUiDisplayMetricsEntry,postToAnalytics,values\", \"bleAlertID\":%{private, location:escape_only}@, \"isFirstUnlocked\":%{private, location:escape_only}@, \"isInLOI\":%{sensitive, location:escape_only}@, \"isLocked\":%{private, location:escape_only}@, \"transport\":%{private, location:escape_only}@, \"userTapped\":%{private, location:escape_only}@, \"postToTapLatency\":%{private, location:escape_only}@, \"serverToPostingLatency\":%{private, location:escape_only}@, \"tapToDisplayLatency\":%{private, location:escape_only}@, \"serverToTapLatency\":%{private, location:escape_only}@, \"isLockedDuringPosting\":%{private, location:escape_only}@, \"isLockedDuringSubmission\":%{private, location:escape_only}@, \"isRelayedAlert\":%{private, location:escape_only}@, \"level\":%{private, location:escape_only}@, \"environmentId\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#aa,downloadCodebook,not supported\"}"
- "{\"msg%{public}.0s\":\"#aa,isSignatureValidUsingCodebook,not supported\"}"
- "{\"msg%{public}.0s\":\"#aa,loadCodebook,not supported\"}"
- "{\"msg%{public}.0s\":\"#aa,setupBgSysTask,not supported\"}"
- "{\"msg%{public}.0s\":\"#cob,invalid codebook dict\"}"
- "{\"msg%{public}.0s\":\"#igv,validate,livability not enabled\"}"
- "{\"msg%{public}.0s\":\"#uimetrics,SAUiDisplayMetricsEntry,postToAnalytics,values\", \"bleAlertID\":%{private, location:escape_only}@, \"isFirstUnlocked\":%{private, location:escape_only}@, \"isInLOI\":%{sensitive, location:escape_only}@, \"isLocked\":%{private, location:escape_only}@, \"transport\":%{private, location:escape_only}@, \"userTapped\":%{private, location:escape_only}@, \"postToTapLatency\":%{private, location:escape_only}@, \"serverToPostingLatency\":%{private, location:escape_only}@, \"tapToDisplayLatency\":%{private, location:escape_only}@, \"serverToTapLatency\":%{private, location:escape_only}@, \"isLockedDuringPosting\":%{private, location:escape_only}@, \"isLockedDuringSubmission\":%{private, location:escape_only}@, \"isRelayedAlert\":%{private, location:escape_only}@, \"level\":%{private, location:escape_only}@}"

```
