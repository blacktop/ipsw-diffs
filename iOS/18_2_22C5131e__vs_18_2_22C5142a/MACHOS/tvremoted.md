## tvremoted

> `/usr/libexec/tvremoted`

```diff

-496.20.20.0.0
-  __TEXT.__text: 0xea70
+496.20.21.0.0
+  __TEXT.__text: 0xeaa8
   __TEXT.__auth_stubs: 0x4e0
   __TEXT.__objc_stubs: 0x22c0
-  __TEXT.__objc_methlist: 0x988
+  __TEXT.__objc_methlist: 0x9a0
   __TEXT.__const: 0xca
-  __TEXT.__oslogstring: 0x1ef7
-  __TEXT.__cstring: 0x822
+  __TEXT.__oslogstring: 0x1f44
+  __TEXT.__cstring: 0x80a
   __TEXT.__gcc_except_tab: 0x1c4
-  __TEXT.__objc_methname: 0x2f6f
+  __TEXT.__objc_methname: 0x2fcd
   __TEXT.__objc_classname: 0x14a
   __TEXT.__objc_methtype: 0xdc1
-  __TEXT.__unwind_info: 0x318
+  __TEXT.__unwind_info: 0x320
   __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__const: 0x6a0
-  __DATA_CONST.__cfstring: 0x680
+  __DATA_CONST.__cfstring: 0x660
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x1738
+  __DATA.__objc_const: 0x1778
   __DATA.__objc_selrefs: 0xb38
-  __DATA.__objc_ivar: 0x7c
+  __DATA.__objc_ivar: 0x80
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x360
   __DATA.__bss: 0x40

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 284
-  Symbols:   2218
-  CStrings:  844
+  Functions: 286
+  Symbols:   2233
+  CStrings:  846
 
Symbols:
+ -[TVRDLaunchEventHandlers requestedModuleEnablement]
+ -[TVRDLaunchEventHandlers setRequestedModuleEnablement:]
+ OBJC_IVAR_$_TVRDLaunchEventHandlers._requestedModuleEnablement
+ __61-[TVRDLaunchEventHandlers _enableTVRemoteControlCenterModule]_block_invoke.56
+ __61-[TVRDLaunchEventHandlers _enableTVRemoteControlCenterModule]_block_invoke.56.cold.1
+ __OBJC_$_INSTANCE_VARIABLES_TVRDLaunchEventHandlers
+ __OBJC_$_PROP_LIST_TVRDLaunchEventHandlers
+ _objc_msgSend$initWithIntent:moduleIdentifier:containerBundleIdentifier:moduleSize:
+ _objc_msgSend$requestedModuleEnablement
+ _objc_msgSend$setRequestedModuleEnablement:
- __61-[TVRDLaunchEventHandlers _enableTVRemoteControlCenterModule]_block_invoke_2.cold.1
- ___61-[TVRDLaunchEventHandlers _enableTVRemoteControlCenterModule]_block_invoke_2
- _objc_msgSend$boolForKey:
- _objc_msgSend$initWithIntent:moduleIdentifier:containerBundleIdentifier:size:
- _objc_msgSend$setBool:forKey:
CStrings:
+ "TB,N,V_requestedModuleEnablement"
+ "TVRemote module already exists in Control Center"
+ "There is an existing request to enable TVRemote CC module in progress. Ignoring this request"
+ "_requestedModuleEnablement"
+ "initWithIntent:moduleIdentifier:containerBundleIdentifier:moduleSize:"
+ "requestedModuleEnablement"
+ "setRequestedModuleEnablement:"
- "AppleTVDetectionRanOnce"
- "Module already enabled once, bailing out without doing anything."
- "boolForKey:"
- "initWithIntent:moduleIdentifier:containerBundleIdentifier:size:"
- "setBool:forKey:"

```
