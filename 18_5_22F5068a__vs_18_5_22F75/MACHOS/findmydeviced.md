## findmydeviced

> `/usr/libexec/findmydeviced`

```diff

 438.35.2.11.19
-  __TEXT.__text: 0x24488c
+  __TEXT.__text: 0x2461d0
   __TEXT.__auth_stubs: 0x1060
-  __TEXT.__objc_stubs: 0x16940
-  __TEXT.__objc_methlist: 0xf7b4
+  __TEXT.__objc_stubs: 0x16b20
+  __TEXT.__objc_methlist: 0xf854
   __TEXT.__const: 0x2cc50
-  __TEXT.__gcc_except_tab: 0x2b80
-  __TEXT.__objc_methname: 0x1c4fe
-  __TEXT.__oslogstring: 0x10ce1
-  __TEXT.__cstring: 0x8b57
-  __TEXT.__objc_classname: 0x1a9c
-  __TEXT.__objc_methtype: 0x30c7
+  __TEXT.__gcc_except_tab: 0x2cb0
+  __TEXT.__objc_methname: 0x1c71f
+  __TEXT.__oslogstring: 0x10e6c
+  __TEXT.__cstring: 0x8c57
+  __TEXT.__objc_classname: 0x1aba
+  __TEXT.__objc_methtype: 0x30fe
   __TEXT.__constg_swiftt: 0x58
   __TEXT.__swift5_typeref: 0x77
   __TEXT.__swift5_reflstr: 0x8

   __TEXT.__swift5_types: 0x4
   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x24
-  __TEXT.__unwind_info: 0x34b0
+  __TEXT.__unwind_info: 0x3508
   __TEXT.__eh_frame: 0x378
   __DATA_CONST.__auth_got: 0x840
-  __DATA_CONST.__got: 0x8f8
+  __DATA_CONST.__got: 0x918
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0xd988
-  __DATA_CONST.__cfstring: 0xa760
-  __DATA_CONST.__objc_classlist: 0x6d0
+  __DATA_CONST.__const: 0xda48
+  __DATA_CONST.__cfstring: 0xa7e0
+  __DATA_CONST.__objc_classlist: 0x6d8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_floatobj: 0x30
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__linkguard: 0xe
-  __DATA.__objc_const: 0x19ee8
-  __DATA.__objc_selrefs: 0x66c8
+  __DATA.__objc_const: 0x19fa0
+  __DATA.__objc_selrefs: 0x6740
   __DATA.__objc_ivar: 0x10cc
-  __DATA.__objc_data: 0x44a0
+  __DATA.__objc_data: 0x44f0
   __DATA.__data: 0x2558
-  __DATA.__bss: 0x7f0
+  __DATA.__bss: 0x800
   __DATA.__common: 0x6c
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5983
-  Symbols:   641
-  CStrings:  8531
+  Functions: 6012
+  Symbols:   645
+  CStrings:  8566
 
Symbols:
+ _FMDSharedConfigurationKeyTheftAndLoss
+ _OBJC_CLASS_$_FMDSharedConfiguration
+ _OBJC_CLASS_$_FMNSXPCConnectionCache
+ _OBJC_CLASS_$_NSLock
CStrings:
+ "-[FMDFMIPXPCServer downloadSharedConfigurationWithLocale:reply:]"
+ "-[FMDFMIPXPCServer getTheftAndLossCoverageWithSerialNumber:reply:]"
+ "Completed T&L update with error: %@"
+ "Current T&L reporting state is %i"
+ "FMDSharedConfigurationManager"
+ "Q32@0:8@16d24"
+ "T&L device coverage %@ for UDID: %@, error: %@"
+ "T&L device coverage %{public}@ for serialNumber: %@, error: %@"
+ "T@\"FMDSharedConfigurationManager\",R,N"
+ "Trigger T&L update with locale: %@"
+ "XPC error for deviceCoverageWithSerialNumber: %li"
+ "_hasSharedConfigurationAccessEntitlement"
+ "brassStatus"
+ "com.apple.icloud.FindMyDevice.FindMyDeviceSharedConfiguration.access"
+ "deviceCoverageWithSerialNumber: %@ timed out"
+ "deviceCoverageWithUDID: %@ timed out"
+ "doNotUseDefaultConfigs"
+ "downloadSharedConfigurationWithLocale:reply:"
+ "entryForConfiguration:deviceClasses:"
+ "getTheftAndLossCoverageWithSerialNumber:reply:"
+ "getTheftAndLossCoverageWithUDID:reply:"
+ "isEnabled"
+ "localeString"
+ "not using default configs"
+ "resumeConnectionWithConfiguration:"
+ "sharedCache"
+ "sharedConfigurationConfiguration"
+ "shouldIncludeTheftAndLossCoverage:covered:"
+ "theftAndLossCoverageWithSerialNumber:"
+ "theftAndLossCoverageWithSerialNumber:timeout:"
+ "theftAndLossCoverageWithUDID:"
+ "theftAndLossCoverageWithUDID:timeout:"
+ "using default configs"
+ "v24@?0Q8@\"NSError\"16"
+ "v32@0:8@\"NSString\"16@?<v@?Q@\"NSError\">24"

```
