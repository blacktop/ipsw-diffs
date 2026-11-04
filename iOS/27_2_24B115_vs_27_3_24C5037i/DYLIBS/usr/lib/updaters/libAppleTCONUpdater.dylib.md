## libAppleTCONUpdater.dylib

> `/usr/lib/updaters/libAppleTCONUpdater.dylib`

```diff

-230.40.6.0.0
-  __TEXT.__text: 0x50c4
-  __TEXT.__cstring: 0x1aec
+230.60.4.0.0
+  __TEXT.__text: 0x63c4
+  __TEXT.__cstring: 0x1dfe
   __TEXT.__const: 0x350
-  __TEXT.__gcc_except_tab: 0x78
-  __TEXT.__unwind_info: 0x238
+  __TEXT.__gcc_except_tab: 0x9c
+  __TEXT.__unwind_info: 0x288
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x180
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x150
-  __AUTH_CONST.__cfstring: 0x7a0
-  __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__auth_got: 0x1e0
+  __AUTH_CONST.__cfstring: 0xb60
+  __AUTH_CONST.__weak_auth_got: 0x20
+  __AUTH_CONST.__auth_got: 0x270
   __DATA.__data: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 109
-  Symbols:   252
-  CStrings:  243
+  - /usr/lib/libz.1.dylib
+  Functions: 123
+  Symbols:   287
+  CStrings:  284
 
Symbols:
+ GCC_except_table4
+ _AppleTCONDPFWCreate
+ _AppleTCONDPFWDestroy
+ _AppleTCONDPFWGetConfig
+ _AppleTCONDPFWGetConfigCount
+ _AppleTCONDPFWGetImage
+ _AppleTCONDPFWGetPayload
+ _AppleTCONDPFWIsMatched
+ _CFArrayGetCount
+ _CFArrayGetTypeID
+ _CFArrayGetValueAtIndex
+ _CFDataCreateMutable
+ _CFDataGetMutableBytePtr
+ _CFDataSetLength
+ _CFStringGetTypeID
+ __ZN20AppleTCONDPUnifiedFW14decompressGzipEPK8__CFData
+ __ZN20AppleTCONDPUnifiedFW16applyBxdiffPatchEPKhmS1_m
+ __ZN20AppleTCONDPUnifiedFWC1EPK8__CFDatajjjj
+ __ZN20AppleTCONDPUnifiedFWC2EPK8__CFDatajjjj
+ __ZN20AppleTCONDPUnifiedFWD1Ev
+ __ZN20AppleTCONDPUnifiedFWD2Ev
+ __ZZN20AppleTCONDPUnifiedFW16applyBxdiffPatchEPKhmS1_mEN11Accumulator5writeEPvPKvy
+ __ZdaPvSt19__type_descriptor_t
+ __ZnamSt19__type_descriptor_t
+ _bzero
+ _dlclose
+ _dlerror
+ _dlopen
+ _dlsym
+ _inflate
+ _inflateEnd
+ _inflateInit2_
+ _malloc_type_realloc
+ _printf
+ _puts
CStrings:
+ "/usr/lib/libParallelCompression.dylib"
+ "1.2.12"
+ "Address"
+ "AppleTCONDPUnifiedFW"
+ "AppleTCONDPUnifiedFW: BXPatch5 failed (result=%d)\n"
+ "AppleTCONDPUnifiedFW: BXPatch5 symbol not found: %s\n"
+ "AppleTCONDPUnifiedFW: gzip ISIZE is zero, file may be corrupt"
+ "AppleTCONDPUnifiedFW: gzip inflate failed, status=%d msg=%s\n"
+ "AppleTCONDPUnifiedFW: gzip input too small (%ld bytes)\n"
+ "AppleTCONDPUnifiedFW: init fails."
+ "AppleTCONDPUnifiedFW: libParallelCompression unavailable: %s\n"
+ "BXPatch5"
+ "BoardID"
+ "Build"
+ "ConfigSubCmd"
+ "Configs"
+ "Configurations"
+ "DeviceID"
+ "Digest"
+ "DirectNVMUpdatePreferred"
+ "FWConfigAPICMD"
+ "FWConfigDigest"
+ "FWConfigs"
+ "FWImg"
+ "FWImgDigest"
+ "HWConfig"
+ "ImageProperties"
+ "Length"
+ "Major"
+ "Minor"
+ "Name"
+ "Option2"
+ "PORUpdatePreferred"
+ "Patches"
+ "ProtectedRegions"
+ "bxdiff"
+ "complete_binary"
+ "major"
+ "patches_policy"
+ "unknown"
+ "version_check_policy"
```
