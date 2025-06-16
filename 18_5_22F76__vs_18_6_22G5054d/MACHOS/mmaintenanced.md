## mmaintenanced

> `/usr/libexec/mmaintenanced`

```diff

-158.100.15.0.0
-  __TEXT.__text: 0x1c034
-  __TEXT.__auth_stubs: 0x12d0
+158.140.2.0.0
+  __TEXT.__text: 0x1d468
+  __TEXT.__auth_stubs: 0x12f0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x124a
-  __TEXT.__oslogstring: 0x2673
-  __TEXT.__cstring: 0x1b28
+  __TEXT.__const: 0x12a0
+  __TEXT.__oslogstring: 0x27b3
+  __TEXT.__cstring: 0x1b78
   __TEXT.__gcc_except_tab: 0x7d0
   __TEXT.__swift5_typeref: 0x9e
-  __TEXT.__objc_methname: 0x1db
+  __TEXT.__objc_methname: 0x1c9
   __TEXT.__swift5_capture: 0x78
   __TEXT.__constg_swiftt: 0x44
   __TEXT.__swift5_fieldmd: 0x50

   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift5_reflstr: 0x24
   __TEXT.__swift5_proto: 0x8
-  __TEXT.__unwind_info: 0x838
+  __TEXT.__unwind_info: 0x850
   __TEXT.__eh_frame: 0x208
-  __DATA_CONST.__auth_got: 0x970
+  __DATA_CONST.__auth_got: 0x980
   __DATA_CONST.__got: 0x230
   __DATA_CONST.__auth_ptr: 0x80
   __DATA_CONST.__const: 0x1018
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0xc8
-  __DATA.__data: 0xed8
-  __DATA.__bss: 0x190
-  __DATA.__common: 0x40
+  __DATA.__objc_selrefs: 0xc0
+  __DATA.__data: 0xe88
+  __DATA.__bss: 0x1a0
+  __DATA.__common: 0x44
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 5DD31519-0F2C-3EB8-9F29-DF43307E3581
-  Functions: 541
-  Symbols:   441
-  CStrings:  476
+  UUID: F44A2332-63FB-343F-A5CD-5B8D86DE268A
+  Functions: 546
+  Symbols:   443
+  CStrings:  483
 
Symbols:
+ _objc_release_x8
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- _$sSi10FoundationEySiSo8NSNumberChcfC
CStrings:
+ "Error: OS updated, but unable to reset OS version data, bailing"
+ "Failed to get UserDefaults database, bailing"
+ "Failed to remove default value for %s, skipping"
+ "MaintenanceTrialOSVersion"
+ "No OS update detected, continuing"
+ "OS has updated, clearing stored default for %s"
+ "OS update has occured, resetting stored OS version"
+ "com.apple.memory-maintenance.vm-trial"
- "initWithLongLong:"

```
