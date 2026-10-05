## ISP.mediacapture

> `/System/Library/MediaCapture/ISP.mediacapture`

```diff

-20.105.6.0.0
-  __TEXT.__text: 0x1eddb4
+20.106.4.0.0
+  __TEXT.__text: 0x1ee5a8
   __TEXT.__init_offsets: 0xc
   __TEXT.__objc_methlist: 0x270
-  __TEXT.__gcc_except_tab: 0x5dcc
-  __TEXT.__const: 0x28dcd
-  __TEXT.__oslogstring: 0x238c7
-  __TEXT.__cstring: 0x1abf7
-  __TEXT.__unwind_info: 0x6840
+  __TEXT.__gcc_except_tab: 0x5dc8
+  __TEXT.__const: 0x28fad
+  __TEXT.__oslogstring: 0x23982
+  __TEXT.__cstring: 0x1accd
+  __TEXT.__unwind_info: 0x6868
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x3bd8
   __AUTH_CONST.__const: 0x2580
-  __AUTH_CONST.__cfstring: 0xac80
+  __AUTH_CONST.__cfstring: 0xace0
   __AUTH_CONST.__objc_const: 0x8a0
   __AUTH_CONST.__weak_auth_got: 0xb0
   __AUTH_CONST.__objc_intobj: 0xd8

   __AUTH_CONST.__auth_got: 0x18c8
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x38
-  __DATA.__data: 0x5756f8
+  __DATA.__data: 0x5b06f8
   __DATA.__common: 0x5e50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 6134
-  Symbols:   7842
-  CStrings:  7111
+  Functions: 6143
+  Symbols:   7851
+  CStrings:  7124
 
Symbols:
+ GCC_except_table457
+ GCC_except_table490
+ GCC_except_table539
+ GCC_except_table542
+ GCC_except_table560
+ GCC_except_table691
+ __ZN3ISP29ISPGraphExclaveSecureDataNode22EnsureBufferPoolsReadyEv
+ __ZN3ISP9ISPDevice19CacheChannelConfigsEj
+ __ZN3ISP9ISPDevice26ISP_CopyChannelConfigCacheEjP21ISPChannelConfigCache
+ __ZN3ISP9ISPDevice29ISP_RefreshChannelConfigCacheEj
+ __ZN3ISP9ISPDevice35InvokeDeviceMessageNotificationProcEjPv
+ __ZN3ISPL24IMX714_setfile_2027_01XXE
+ __ZN3ISPL24IMX914_setfile_2327_01XXE
+ __ZN3ISPL24IMX914_setfile_2327_02XXE
- GCC_except_table488
- GCC_except_table537
- GCC_except_table540
- GCC_except_table558
- GCC_except_table688
CStrings:
+ "%s - Error reading kernel config cache - chan: %d, res: 0x%08X\n"
+ "%s - [Exclaves]: [ERROR]: ch%u: buffer pools unavailable, dropping frame %u\n"
+ "%s - channel configs not valid - exiting\n"
+ "%s - kernel config count %d != firmware %d - chan: %d\n"
+ "/usr/local/share/firmware/isp/2027_01XX.dat"
+ "/usr/local/share/firmware/isp/2327_01XX.dat"
+ "/usr/local/share/firmware/isp/2327_02XX.dat"
+ "AECounter_Private"
+ "CacheChannelConfigs"
+ "Could not find %s as %s (errno: %d)"
+ "EnsureBufferPoolsReady"
+ "Found %s at %s."
+ "ISPCaptureStreamStart - EnableDolbyVisionMetadata error: 0x%08X\n\n"
+ "Will use ISP references"
+ "Will use SEP references"
+ "sparse reference plist"
+ "sparseLP reference plist"
- "%s - Error getting LSC polynomial - chan: %d, res: 0x%08X\n"
- "%s - Error getting camera config - chan: %d, res: 0x%08X\n"
- "Could not find reference plist at %s (errno: %d). Will use ISP references"
- "Found reference plist at %s. Will use SEP references"
```
