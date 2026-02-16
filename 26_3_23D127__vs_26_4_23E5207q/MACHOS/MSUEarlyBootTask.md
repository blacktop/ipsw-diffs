## MSUEarlyBootTask

> `/usr/libexec/MSUEarlyBootTask`

```diff

-2422.80.9.0.2
-  __TEXT.__text: 0x3bc0
-  __TEXT.__auth_stubs: 0x720
+2422.100.179.0.3
+  __TEXT.__text: 0x3cc4
+  __TEXT.__auth_stubs: 0x740
   __TEXT.__objc_stubs: 0x420
-  __TEXT.__cstring: 0x27f1
+  __TEXT.__cstring: 0x279d
   __TEXT.__const: 0x444
   __TEXT.__objc_methname: 0x2e8
-  __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x398
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__auth_got: 0x3a8
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x10
-  __DATA_CONST.__cfstring: 0x380
+  __DATA_CONST.__cfstring: 0x3c0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
-  UUID: 2DC452AC-FF82-361E-AAF4-35D8E71A4B17
-  Functions: 23
-  Symbols:   310
-  CStrings:  319
+  UUID: 1D8E8CC2-D30C-359F-BB95-493E93DCDE8D
+  Functions: 25
+  Symbols:   326
+  CStrings:  320
 
Symbols:
+ /AppleInternal/Library/BuildRoots/4~CIsPugBy0fWCEpLfTSqIgtTZJvXk_Nzzu8ks5bw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
+ /Library/Caches/com.apple.xbs/1B2D3EE6-84B2-433C-9046-2E1EE5F907EE/TemporaryDirectory.PsSXco/Sources/PurpleRestore_libpartition/ramrod/
+ /Library/Caches/com.apple.xbs/7402B4CC-18BB-4CD4-BF13-EC385A655759/TemporaryDirectory.psCVfe/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUEarlyBootTask.build/Objects-normal/arm64e/MSUEarlyBootTask.o
+ /Library/Caches/com.apple.xbs/7402B4CC-18BB-4CD4-BF13-EC385A655759/TemporaryDirectory.psCVfe/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUEarlyBootTask.build/Objects-normal/arm64e/MSUPerformanceUtils.o
+ /Library/Caches/com.apple.xbs/7402B4CC-18BB-4CD4-BF13-EC385A655759/TemporaryDirectory.psCVfe/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUEarlyBootTask.build/Objects-normal/arm64e/cleanup_uuidtext.o
+ /Library/Caches/com.apple.xbs/7402B4CC-18BB-4CD4-BF13-EC385A655759/TemporaryDirectory.psCVfe/Sources/MobileSoftwareUpdate/
+ /Library/Caches/com.apple.xbs/7402B4CC-18BB-4CD4-BF13-EC385A655759/TemporaryDirectory.psCVfe/Sources/MobileSoftwareUpdate/MSUEarlyBootTask/
+ MSUPerformanceUtils.m
+ _enable_rapid_vnode_aging
+ _logfunction
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x27
+ _objc_retain_x28
- /AppleInternal/Library/BuildRoots/4~CHzkugD8rBQWZWQMLudMMj0gwYLr6vMC_AyM7MM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
- /Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUEarlyBootTask.build/Objects-normal/arm64e/MSUEarlyBootTask.o
- /Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUEarlyBootTask.build/Objects-normal/arm64e/cleanup_uuidtext.o
- /Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/
- /Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/MSUEarlyBootTask/
- /Library/Caches/com.apple.xbs/Sources/PurpleRestore_libpartition/ramrod/
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x25
- _objc_retain_x8
CStrings:
+ "Failed to enable vnode rapid aging: %s (%d)\n"
+ "Successfully enabled rapid vnode aging\n\n"
- "%s: MSUEarlyBootTask: Enabling vnode rapid aging\n"
- "%s: MSUEarlyBootTask: Failed to enable vnode rapid aging\n"
- "%s: MSUEarlyBootTask: Successfully enabled rapid vnode aging\n"

```
