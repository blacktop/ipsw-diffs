## com.apple.accessoryd.matching

> `/System/Library/UserEventPlugins/com.apple.accessoryd.matching.plugin/com.apple.accessoryd.matching`

```diff

-898.80.3.0.0
-  __TEXT.__text: 0x393a8
+919.100.33.0.0
+  __TEXT.__text: 0x393f4
   __TEXT.__auth_stubs: 0xef0
   __TEXT.__objc_stubs: 0x4640
   __TEXT.__objc_methlist: 0x1b88
-  __TEXT.__cstring: 0x3fd8
-  __TEXT.__objc_methname: 0x6024
+  __TEXT.__cstring: 0x40ac
+  __TEXT.__objc_methname: 0x6038
   __TEXT.__objc_classname: 0x26c
   __TEXT.__objc_methtype: 0xaaa
   __TEXT.__const: 0x84

   __DATA.__auth_got: 0x788
   __DATA.__got: 0x140
   __DATA.__auth_ptr: 0x10
-  __DATA.__const: 0xd58
-  __DATA.__cfstring: 0x2ec0
+  __DATA.__const: 0xde8
+  __DATA.__cfstring: 0x3000
   __DATA.__objc_classlist: 0x98
   __DATA.__objc_catlist: 0x10
   __DATA.__objc_protolist: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 719AEE30-37C6-31B8-A04B-BFEEA577D120
+  UUID: 6BDE5F71-0D2E-3134-9E9B-E2D8C641F7EB
   Functions: 1261
-  Symbols:   7627
-  CStrings:  2580
+  Symbols:   7663
+  CStrings:  2601
 
Symbols:
+ _ACCUserDefaultsKey_ForceAccInfoUpdateRelaySupport
+ _ACCUserDefaultsKey_ForceMFi4AuthOverNFC
+ _ACCUserDefaultsKey_IgnoreAccInfoUpdateRelaySupport
+ _ACCUserDefaultsKey_IgnoreAuthReset
+ _ACCUserDefaultsKey_MFi4ECDSADisallow
+ _ACCUserDefaultsKey_MFi4ECDSAOnly
+ _ACCUserDefaultsKey_MFi4SigmaIRequired
+ _ACCUserDefaultsKey_PacketLoggingPlainTextOnly
+ _ACCUserDefaultsKey_PretendNoDeviceIdentityCerts
+ __39-[IOUIAngelService initWithIdentifier:]_block_invoke.57
+ __39-[IOUIAngelService initWithIdentifier:]_block_invoke.57.cold.1
+ __IOAccessoryManagerEventCallback_block_invoke.829
+ __IOAccessoryManagerEventCallback_block_invoke.829.cold.1
+ __IOAccessoryManagerEventCallback_block_invoke.830.cold.1
+ __IOAccessoryManagerEventCallback_block_invoke.831
+ __IOAccessoryManagerEventCallback_block_invoke.832
+ __IOAccessoryManagerEventCallback_block_invoke.834
+ ___presentUnlockDialog_block_invoke.907
+ ___presentUnlockDialog_block_invoke.907.cold.1
+ ___presentUnlockDialog_block_invoke.914
+ ___presentUnlockDialog_block_invoke.914.cold.1
+ ___presentUnlockDialog_block_invoke.914.cold.2
+ ___presentUnlockDialog_block_invoke.917
+ ___presentUnlockDialog_block_invoke.917.cold.1
+ ___presentUnlockDialog_block_invoke.917.cold.2
+ ___presentUnlockDialog_block_invoke.917.cold.3
+ ___presentUnlockDialog_block_invoke.917.cold.4
+ __block_literal_global.226
+ __block_literal_global.229
+ __block_literal_global.231
+ __block_literal_global.322
+ __block_literal_global.360
+ __block_literal_global.854
+ __block_literal_global.856
+ __block_literal_global.865
+ __block_literal_global.882
+ __block_literal_global.885
+ __block_literal_global.887
+ __block_literal_global.904
+ __block_literal_global.906
+ __block_literal_global.909
+ __block_literal_global.916
+ __block_literal_global.919
+ __block_literal_global.921
+ __block_literal_global.942
+ __serviceLDCMMitigationStatusChanged_block_invoke.883
+ __serviceLDCMMitigationStatusChanged_block_invoke.883.cold.1
+ __serviceLDCMMitigationStatusChanged_block_invoke.883.cold.2
+ __serviceLDCMMitigationStatusChanged_block_invoke.883.cold.3
+ __serviceLDCMMitigationStatusChanged_block_invoke.883.cold.4
+ _kCFACCUserDefaultsKey_ForceAccInfoUpdateRelaySupport
+ _kCFACCUserDefaultsKey_ForceMFi4AuthOverNFC
+ _kCFACCUserDefaultsKey_IgnoreAccInfoUpdateRelaySupport
+ _kCFACCUserDefaultsKey_IgnoreAuthReset
+ _kCFACCUserDefaultsKey_MFi4ECDSADisallow
+ _kCFACCUserDefaultsKey_MFi4ECDSAOnly
+ _kCFACCUserDefaultsKey_MFi4SigmaIRequired
+ _kCFACCUserDefaultsKey_PacketLoggingPlainTextOnly
+ _kCFACCUserDefaultsKey_PretendNoDeviceIdentityCerts
+ _unnamed_array_storage.255
- __39-[IOUIAngelService initWithIdentifier:]_block_invoke.56
- __39-[IOUIAngelService initWithIdentifier:]_block_invoke.56.cold.1
- __IOAccessoryManagerEventCallback_block_invoke.825
- __IOAccessoryManagerEventCallback_block_invoke.825.cold.1
- __IOAccessoryManagerEventCallback_block_invoke.826
- __IOAccessoryManagerEventCallback_block_invoke.826.cold.1
- __IOAccessoryManagerEventCallback_block_invoke.827
- __IOAccessoryManagerEventCallback_block_invoke.828
- ___presentUnlockDialog_block_invoke.903
- ___presentUnlockDialog_block_invoke.903.cold.1
- ___presentUnlockDialog_block_invoke.906
- ___presentUnlockDialog_block_invoke.906.cold.1
- ___presentUnlockDialog_block_invoke.906.cold.2
- ___presentUnlockDialog_block_invoke.913
- ___presentUnlockDialog_block_invoke.913.cold.1
- ___presentUnlockDialog_block_invoke.913.cold.2
- ___presentUnlockDialog_block_invoke.913.cold.3
- ___presentUnlockDialog_block_invoke.913.cold.4
- __block_literal_global.202
- __block_literal_global.204
- __block_literal_global.223
- __block_literal_global.321
- __block_literal_global.359
- __block_literal_global.850
- __block_literal_global.852
- __block_literal_global.861
- __block_literal_global.878
- __block_literal_global.881
- __block_literal_global.883
- __block_literal_global.898
- __block_literal_global.900
- __block_literal_global.905
- __block_literal_global.908
- __block_literal_global.915
- __block_literal_global.917
- __block_literal_global.938
- __serviceLDCMMitigationStatusChanged_block_invoke.879
- __serviceLDCMMitigationStatusChanged_block_invoke.879.cold.1
- __serviceLDCMMitigationStatusChanged_block_invoke.879.cold.2
- __serviceLDCMMitigationStatusChanged_block_invoke.879.cold.3
- __serviceLDCMMitigationStatusChanged_block_invoke.879.cold.4
- _unnamed_array_storage.252
CStrings:
+ "ForceAccInfoUpdateRelaySupport"
+ "ForceMFi4AuthOverNFC"
+ "IgnoreAccInfoUpdateRelaySupport"
+ "IgnoreAuthReset"
+ "MFi4ECDSADisallow"
+ "MFi4ECDSAOnly"
+ "MFi4SigmaIRequired"
+ "PacketLoggingPlainTextOnly"
+ "PretendNoDeviceIdentityCerts"
+ "T@\"NSString\",?,R,C"
+ "iPad"

```
