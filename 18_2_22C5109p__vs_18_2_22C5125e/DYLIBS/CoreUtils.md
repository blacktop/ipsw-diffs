## CoreUtils

> `/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils`

```diff

-760.26.0.0.0
-  __TEXT.__text: 0x1141dc
-  __TEXT.__auth_stubs: 0x2e50
-  __TEXT.__objc_methlist: 0x82d0
-  __TEXT.__const: 0x2140
-  __TEXT.__gcc_except_tab: 0x1ac4
-  __TEXT.__cstring: 0x233f0
-  __TEXT.__oslogstring: 0x32c
-  __TEXT.__unwind_info: 0x3950
+760.34.0.0.0
+  __TEXT.__text: 0x114a30
+  __TEXT.__auth_stubs: 0x2eb0
+  __TEXT.__objc_methlist: 0x8340
+  __TEXT.__const: 0x2150
+  __TEXT.__gcc_except_tab: 0x1b18
+  __TEXT.__cstring: 0x233ee
+  __TEXT.__oslogstring: 0x3c2
+  __TEXT.__unwind_info: 0x3988
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0xbe3
-  __TEXT.__objc_methname: 0x14b01
-  __TEXT.__objc_methtype: 0x3fd0
-  __TEXT.__objc_stubs: 0x9cc0
+  __TEXT.__objc_classname: 0xbeb
+  __TEXT.__objc_methname: 0x14bf5
+  __TEXT.__objc_methtype: 0x4005
+  __TEXT.__objc_stubs: 0x9d60
   __DATA_CONST.__got: 0x638
-  __DATA_CONST.__const: 0x2928
-  __DATA_CONST.__objc_classlist: 0x2f8
+  __DATA_CONST.__const: 0x2990
+  __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x40b8
+  __DATA_CONST.__objc_selrefs: 0x4100
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x208
-  __AUTH_CONST.__auth_got: 0x1738
+  __AUTH_CONST.__auth_got: 0x1768
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x1f30
-  __AUTH_CONST.__cfstring: 0x4260
-  __AUTH_CONST.__objc_const: 0x154e0
+  __AUTH_CONST.__const: 0x1f50
+  __AUTH_CONST.__cfstring: 0x42c0
+  __AUTH_CONST.__objc_const: 0x155e0
   __AUTH_CONST.__objc_intobj: 0x240
-  __AUTH.__objc_data: 0x1b30
+  __AUTH.__objc_data: 0x1b80
   __AUTH.__data: 0xb20
-  __DATA.__objc_ivar: 0x14c4
+  __DATA.__objc_ivar: 0x14d0
   __DATA.__data: 0x3370
   __DATA.__bss: 0x10b8
   __DATA.__common: 0x2a
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__data: 0x178
-  __DATA_DIRTY.__bss: 0x218
+  __DATA_DIRTY.__bss: 0x221
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5693
-  Symbols:   6709
-  CStrings:  9444
+  Functions: 5706
+  Symbols:   6730
+  CStrings:  9467
 
Symbols:
+ _OBJC_CLASS_$_CUOPACK
+ _OBJC_METACLASS_$_CUOPACK
+ __os_log_debug_impl
+ _nw_path_monitor_cancel
+ _nw_path_monitor_create
+ _nw_path_monitor_set_queue
+ _nw_path_monitor_set_update_handler
+ _nw_path_monitor_start
CStrings:
+ "-[CUVoiceSession _speakText:flags:volume:completion:]"
+ "@\"NSObject<OS_nw_path_monitor>\""
+ "Activate: mode=%!@(MISSING), url=%!@(MISSING), timeout=%!f(MISSING) seconds"
+ "CUOPACK"
+ "Captive network detected"
+ "Captive network state: detected=%!{(MISSING)bool}d"
+ "Path monitor update: path=%!@(MISSING)"
+ "Tq,N,V_mode"
+ "_captiveDetectedCheck"
+ "_captiveNotifyToken"
+ "_mode"
+ "_pathMonitor"
+ "_pathMonitorStart"
+ "_pathMonitorUpdated:"
+ "_speakText:flags:volume:completion:"
+ "com.apple.coreutils.captive-network-state"
+ "dealloc: active"
+ "dealloc: inactive"
+ "decodeData:flags:error:"
+ "encodeObject:flags:error:"
+ "full"
+ "mode"
+ "partial"
+ "setMode:"
+ "setPlaybackVolume:"
+ "speakText:flags:volume:completionHandler:"
+ "v44@0:8@16I24d28@?36"
- "-[CUReachabilityMonitor _activate]"
- "-[CUVoiceSession _speakText:flags:completion:]"
- "Activate <%!@(MISSING)>, %!f(MISSING) second timeout\n"
- "Activate <%!@(MISSING)>, no timeout\n"
- "_speakText:flags:completion:"

```
