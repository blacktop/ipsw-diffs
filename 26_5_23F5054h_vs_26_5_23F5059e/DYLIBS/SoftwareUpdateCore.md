## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

```diff

-2422.120.23.0.0
-  __TEXT.__text: 0xb71ac
-  __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_methlist: 0x7bbc
+2422.120.23.0.9
+  __TEXT.__text: 0xb7a28
+  __TEXT.__auth_stubs: 0xce0
+  __TEXT.__objc_methlist: 0x7c34
   __TEXT.__const: 0x1c2
-  __TEXT.__cstring: 0x1552d
-  __TEXT.__oslogstring: 0xc7b3
+  __TEXT.__cstring: 0x1569d
+  __TEXT.__oslogstring: 0xc843
   __TEXT.__gcc_except_tab: 0x754
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__constg_swiftt: 0x50

   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0x2038
   __TEXT.__objc_classname: 0x7da
-  __TEXT.__objc_methname: 0x15d63
+  __TEXT.__objc_methname: 0x15e99
   __TEXT.__objc_methtype: 0xff8
-  __TEXT.__objc_stubs: 0xece0
-  __DATA_CONST.__got: 0xa80
+  __TEXT.__objc_stubs: 0xee20
+  __DATA_CONST.__got: 0xa90
   __DATA_CONST.__const: 0x23d8
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4530
+  __DATA_CONST.__objc_selrefs: 0x4580
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__auth_got: 0x670
+  __AUTH_CONST.__auth_got: 0x680
   __AUTH_CONST.__const: 0x4e8
-  __AUTH_CONST.__cfstring: 0x12d00
-  __AUTH_CONST.__objc_const: 0xac10
+  __AUTH_CONST.__cfstring: 0x12e20
+  __AUTH_CONST.__objc_const: 0xac80
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH.__objc_data: 0x750
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x9d8
+  __DATA.__objc_ivar: 0x9e0
   __DATA.__data: 0x398
   __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0xcd0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F3A45A69-5C63-34ED-9660-1065BBBDF648
-  Functions: 3101
-  Symbols:   10658
-  CStrings:  9095
+  UUID: 04756DE0-3FF0-38A7-993A-3DC137671BC2
+  Functions: 3109
+  Symbols:   10690
+  CStrings:  9130
 
Symbols:
+ -[SUCorePolicy majorDelayPeriodDays]
+ -[SUCorePolicy minorDelayPeriodDays]
+ -[SUCorePolicyExtensionManagedUpdates majorDelayPeriodDays]
+ -[SUCorePolicyExtensionManagedUpdates majorDelayPeriodSecs]
+ -[SUCorePolicyExtensionManagedUpdates minorDelayPeriodDays]
+ -[SUCorePolicyExtensionManagedUpdates minorDelayPeriodSecs]
+ -[SUCorePolicyExtensionManagedUpdates setMajorDelayPeriodSecs:]
+ -[SUCorePolicyExtensionManagedUpdates setMinorDelayPeriodSecs:]
+ _CFDateGetTypeID
+ _OBJC_IVAR_$_SUCorePolicyExtensionManagedUpdates._majorDelayPeriodSecs
+ _OBJC_IVAR_$_SUCorePolicyExtensionManagedUpdates._minorDelayPeriodSecs
+ _kSUCoreControllerMajorDelayPeriodKey
+ _kSUCoreControllerMinorDelayPeriodKey
+ _objc_msgSend$majorDelayPeriod
+ _objc_msgSend$majorDelayPeriodDays
+ _objc_msgSend$majorDelayPeriodSecs
+ _objc_msgSend$minorDelayPeriod
+ _objc_msgSend$minorDelayPeriodDays
+ _objc_msgSend$minorDelayPeriodSecs
+ _objc_msgSend$setMajorDelayPeriod:
+ _objc_msgSend$setMajorDelayPeriodSecs:
+ _objc_msgSend$setMinorDelayPeriod:
+ _objc_msgSend$setMinorDelayPeriodSecs:
+ _os_variant_allows_internal_security_policies
CStrings:
+ "%@ with MDMUseDelayPeriod, yet delayPeriodSecs,minorDelayPeriodSecs,majorDelayPeriodSecs < 0 (ignoring delay period)"
+ "%@(supervised:%@|requestedPMV:%@|MDMUseDelayPeriod:%@|delayPeriodSecs:%ld|minorDelayPeriodSecs:%ld|majorDelayPeriodSecs=%ld|mdmSoftwareUpdatePath:%@)"
+ "%@:%ld|"
+ "%@:%ld|%@:%ld"
+ "%{public}@ Override major descriptor releaseDate from %{public}@ to %{public}@"
+ "%{public}@ Override minor descriptor releaseDate from %{public}@ to %{public}@"
+ "MajorDelayPeriod"
+ "MajorDelayPeriodSecs"
+ "MinorDelayPeriod"
+ "MinorDelayPeriodSecs"
+ "SpoofMajorDescriptorReleaseDate"
+ "SpoofMinorDescriptorReleaseDate"
+ "Tq,N,V_majorDelayPeriodSecs"
+ "Tq,N,V_minorDelayPeriodSecs"
+ "_majorDelayPeriodSecs"
+ "_minorDelayPeriodSecs"
+ "com.apple.MobileSoftwareUpdate"
+ "majorDelayPeriod"
+ "majorDelayPeriodDays"
+ "majorDelayPeriodSecs"
+ "minorDelayPeriod"
+ "minorDelayPeriod:%ld|majorDelayPeriod:%ld"
+ "minorDelayPeriodDays"
+ "minorDelayPeriodSecs"
+ "setMajorDelayPeriod:"
+ "setMajorDelayPeriodSecs:"
+ "setMinorDelayPeriod:"
+ "setMinorDelayPeriodSecs:"
+ "|MDM DelayPeriod=%ld, MinorDelayPeriod=%ld, MajorDelayPeriod=%ld"
- "%@ with MDMUseDelayPeriod, yet delayPeriodSecs < 0 (ignoring delay period)"
- "%@(supervised:%@|requestedPMV:%@|MDMUseDelayPeriod:%@|delayPeriodSecs:%ld|mdmSoftwareUpdatePath:%@)"
- "|MDMDelay=%ld"

```
