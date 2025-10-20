## SafariSafeBrowsing

> `/System/Library/PrivateFrameworks/SafariSafeBrowsing.framework/SafariSafeBrowsing`

```diff

-622.2.10.10.1
-  __TEXT.__text: 0x6025c
-  __TEXT.__auth_stubs: 0xf80
-  __TEXT.__objc_methlist: 0xb2c
-  __TEXT.__gcc_except_tab: 0x6844
-  __TEXT.__cstring: 0x1986
+622.2.11.10.4
+  __TEXT.__text: 0x607bc
+  __TEXT.__auth_stubs: 0xf90
+  __TEXT.__objc_methlist: 0xb34
+  __TEXT.__gcc_except_tab: 0x68fc
+  __TEXT.__cstring: 0x19b1
   __TEXT.__const: 0x298
-  __TEXT.__oslogstring: 0x1d9a
-  __TEXT.__unwind_info: 0x2bd0
+  __TEXT.__oslogstring: 0x1e0e
+  __TEXT.__unwind_info: 0x2be8
   __TEXT.__objc_classname: 0x217
-  __TEXT.__objc_methname: 0x24f3
+  __TEXT.__objc_methname: 0x2579
   __TEXT.__objc_methtype: 0x11c8
-  __TEXT.__objc_stubs: 0x1820
+  __TEXT.__objc_stubs: 0x18c0
   __DATA_CONST.__got: 0x248
-  __DATA_CONST.__const: 0x758
+  __DATA_CONST.__const: 0x778
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x938
+  __DATA_CONST.__objc_selrefs: 0x960
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x7d8
-  __AUTH_CONST.__const: 0x2808
-  __AUTH_CONST.__cfstring: 0x1220
+  __AUTH_CONST.__auth_got: 0x7e0
+  __AUTH_CONST.__const: 0x2828
+  __AUTH_CONST.__cfstring: 0x1260
   __AUTH_CONST.__objc_const: 0x18f0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0xa0
   __DATA.__data: 0x300
-  __DATA.__bss: 0x48
+  __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__bss: 0x3a8
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 289CE46D-F7C6-3CB5-BCBE-387947AFC757
-  Functions: 2274
-  Symbols:   6678
-  CStrings:  1080
+  UUID: 50590502-02F8-3DBF-BBE9-9B8A62BAC5FB
+  Functions: 2278
+  Symbols:   6697
+  CStrings:  1091
 
Symbols:
+ -[RemoteConfigurationController _launchTimeBasedPercentile]
+ -[RemoteConfigurationController _launchTimeBasedPercentile].cold.1
+ GCC_except_table85
+ __ZN7Backend6Google15DatabaseUpdater30copyBundledDatabaseIfAvailableERKNS0_12DatabaseInfoE
+ __ZZ59-[RemoteConfigurationController _launchTimeBasedPercentile]E10percentile
+ __ZZ59-[RemoteConfigurationController _launchTimeBasedPercentile]E4once
+ ___59-[RemoteConfigurationController _launchTimeBasedPercentile]_block_invoke
+ ____ZN7Backend6Google15DatabaseUpdater19fetchEncodedUpdatesENS0_19DatabaseUpdateStyleEP18ProxyConfiguration_block_invoke.132
+ ____ZN7Backend6Google15DatabaseUpdater19fetchEncodedUpdatesENS0_19DatabaseUpdateStyleEP18ProxyConfiguration_block_invoke.133
+ _gettimeofday
+ _objc_msgSend$_launchTimeBasedPercentile
+ _objc_msgSend$copyItemAtPath:toPath:error:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$pathForResource:ofType:inDirectory:
+ _objc_msgSend$unsignedIntegerValue
+ _percentageToApplyToKey
- GCC_except_table155
- GCC_except_table157
- GCC_except_table96
- ____ZN7Backend6Google15DatabaseUpdater19fetchEncodedUpdatesENS0_19DatabaseUpdateStyleEP18ProxyConfiguration_block_invoke.127
- ____ZN7Backend6Google15DatabaseUpdater19fetchEncodedUpdatesENS0_19DatabaseUpdateStyleEP18ProxyConfiguration_block_invoke.128
CStrings:
+ "BundledDatabases/%@"
+ "Copied bundled database '%{public}s' from bundle resources"
+ "Failed to copy bundled database '%{public}s': %{public}@"
+ "Percentage To Apply To"
+ "_launchTimeBasedPercentile"
+ "copyItemAtPath:toPath:error:"
+ "localizedDescription"
+ "pathForResource:ofType:inDirectory:"
+ "unsignedIntegerValue"

```
