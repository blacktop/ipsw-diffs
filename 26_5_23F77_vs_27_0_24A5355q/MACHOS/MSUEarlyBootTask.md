## MSUEarlyBootTask

> `/usr/libexec/MSUEarlyBootTask`

```diff

-2422.120.23.0.9
-  __TEXT.__text: 0x3cc4
-  __TEXT.__auth_stubs: 0x740
+2717.0.0.0.0
+  __TEXT.__text: 0x3c6c
+  __TEXT.__auth_stubs: 0x730
   __TEXT.__objc_stubs: 0x420
   __TEXT.__cstring: 0x279d
   __TEXT.__const: 0x444
   __TEXT.__objc_methname: 0x2e8
   __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x3a8
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x10
   __DATA_CONST.__cfstring: 0x3c0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__auth_got: 0x3a0
+  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_selrefs: 0x108
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
-  UUID: 386CF855-398C-3C67-B3C5-8627E875807A
+  UUID: 7D7CA6A3-5CE0-3376-A141-F35525E04A54
   Functions: 25
-  Symbols:   326
+  Symbols:   325
   CStrings:  320
 
Symbols:
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUEarlyBootTask.build/Objects-normal/arm64e/MSUEarlyBootTask.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUEarlyBootTask.build/Objects-normal/arm64e/MSUPerformanceUtils.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUEarlyBootTask.build/Objects-normal/arm64e/cleanup_uuidtext.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Sources/MobileSoftwareUpdate/
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Sources/MobileSoftwareUpdate/MSUEarlyBootTask/
+ /Library/Caches/com.apple.xbs/63EA7F73-24CA-4FFF-9299-E066706F6743/TemporaryDirectory.oDpNrv/Sources/PurpleRestore_libpartition/ramrod/
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x25
+ _objc_retain_x8
+ _os_variant_is_recovery
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUEarlyBootTask.build/Objects-normal/arm64e/MSUEarlyBootTask.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUEarlyBootTask.build/Objects-normal/arm64e/MSUPerformanceUtils.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUEarlyBootTask.build/Objects-normal/arm64e/cleanup_uuidtext.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Sources/MobileSoftwareUpdate/
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Sources/MobileSoftwareUpdate/MSUEarlyBootTask/
- /Library/Caches/com.apple.xbs/38935958-B363-4332-8EB1-E5B8F06DAD22/TemporaryDirectory.qF9DnN/Sources/PurpleRestore_libpartition/ramrod/
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x27
- _objc_retain_x28
Functions:
~ _MSUCleanupUUIDTextFolder : 104 -> 96
~ _debugv : 160 -> 156
~ _logString : 304 -> 292
~ _MSUEarlyBootTaskSetupACLForPath : 668 -> 648
~ _moveFolderContentsIfItExists : 656 -> 652
~ _main : 8376 -> 8336

```
