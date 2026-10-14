## CoreThreadCommissionerServiced

> `/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__objc_methtype`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-446.0.2.0.1
-  __TEXT.__text: 0x6f01c
-  __TEXT.__auth_stubs: 0x1700
-  __TEXT.__objc_stubs: 0x38c0
+446.0.4.0.0
+  __TEXT.__text: 0x6fa5c
+  __TEXT.__auth_stubs: 0x1710
+  __TEXT.__objc_stubs: 0x38e0
   __TEXT.__objc_methlist: 0x2524
-  __TEXT.__cstring: 0xa353
-  __TEXT.__objc_methname: 0x61c5
+  __TEXT.__cstring: 0xa5e3
+  __TEXT.__objc_methname: 0x61df
   __TEXT.__objc_classname: 0x357
   __TEXT.__objc_methtype: 0x1975
-  __TEXT.__const: 0x742
-  __TEXT.__gcc_except_tab: 0x1c04
-  __TEXT.__oslogstring: 0xae19
+  __TEXT.__const: 0x762
+  __TEXT.__gcc_except_tab: 0x1c18
+  __TEXT.__oslogstring: 0xb183
   __TEXT.__swift5_typeref: 0x4c2
   __TEXT.__swift5_capture: 0x418
   __TEXT.__swift5_fieldmd: 0xac

   __TEXT.__swift_as_entry: 0x6c
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift_as_cont: 0x154
-  __TEXT.__unwind_info: 0x21c0
+  __TEXT.__unwind_info: 0x21c8
   __TEXT.__eh_frame: 0x15c8
   __DATA_CONST.__const: 0x18e0
-  __DATA_CONST.__cfstring: 0x1b60
+  __DATA_CONST.__cfstring: 0x1c80
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__auth_got: 0xb98
+  __DATA_CONST.__auth_got: 0xba0
   __DATA_CONST.__got: 0x490
   __DATA_CONST.__auth_ptr: 0x138
   __DATA.__objc_const: 0x3118
-  __DATA.__objc_selrefs: 0x13a0
+  __DATA.__objc_selrefs: 0x13a8
   __DATA.__objc_ivar: 0xc0
   __DATA.__objc_data: 0x600
   __DATA.__data: 0x700

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1851
-  Symbols:   566
-  CStrings:  2823
+  Functions: 1850
+  Symbols:   567
+  CStrings:  2851
 
Symbols:
+ _$s7Network9NWBrowserC10DescriptorO7OptionsV10DeviceTypeV13homeAccessoryAIvgZ
CStrings:
+ "%02x"
+ "%s: #MOS : ==> Dataset is nil or empty, Line : %d"
+ "%s: #MOS : ==> Decoded TLV, format is invalid, cannot read length, Line : %d"
+ "%s: #MOS : ==> Duplicate type is detected : %d, Line : %d"
+ "%s: #MOS : ==> Invalid dataset length %d, max is %d, Line : %d"
+ "%s: #MOS : ==> Invalid dataset length %lu, max is %d, Line : %d"
+ "%s: #MOS : Channel Mask : %@"
+ "%s: #MOS : Mesh Local Prefix : %@"
+ "%s: #MOS : Security Policy : %@"
+ "%s: %d: Warning : dataset is incomplete : ml_prefix : %@, sec_policy : %@, channel_mask : %@"
+ "%s: Active Timestamp TLV holds OpenThread's invalid encoding (all ones), treating as absent"
+ "%s:%d: Incoming record supersedes the preferred network, allowing the store"
+ "%s:%d: Rejecting store - %{public}@"
+ "%s:%d: This preferred network entry has a record associated with it, record name : %@, dataset length : %lu, dataset : %{sensitive}s, check if it is frozen or not"
+ "%s:%d: precedence check skipped - dataset could not be parsed (stored:%d incoming:%d)"
+ "(empty)"
+ "-[THThreadNetworkCredentialsKeychainBackingStore areValidDataSetTLVs:creds:updateATS:isATSAppended:]"
+ "-[THThreadNetworkCredentialsStoreLocalClient validateDataSetStructure:]"
+ "==> Invalid dataset length %d, max is %d"
+ "Active Operational Dataset is invalid or incomplete"
+ "Active Timestamp"
+ "B40@0:8C16C20r*24Q32"
+ "BOOL thInspectDataSet(NSData * _Nonnull __strong, THDataSetTlvFlags * _Nonnull, BOOL * _Nonnull, uint64_t * _Nonnull)"
+ "DSTR:%s channel high byte is not zero:%d"
+ "DSTR:%s is out of range:%d"
+ "DSTR:%s page is not zero:%d"
+ "DSTR:Channel Mask entry format is invalid"
+ "DSTR:Channel Mask entry length is not 4:%d"
+ "DSTR:Channel Mask page is neither 0 nor 2:%d"
+ "DSTR:Invalid %s length:%d"
+ "DSTR:Invalid Mesh Local Prefix length:%d"
+ "DSTR:Invalid Mesh Local Prefix, first byte is 0x%02x, expected 0x%02x"
+ "DSTR:Invalid Network Name length:%d"
+ "DSTR:Invalid PAN ID length:%d"
+ "DSTR:Invalid PAN ID, broadcast value is not allowed"
+ "DSTR:Invalid Security Policy length:%d"
+ "DSTR:Invalid Security Policy rotation time of zero"
+ "DSTR:TLV type %d declares length %d but only %zu bytes available"
+ "Dropped %lu of %lu stored active data set record(s) that could not be deserialized"
+ "Error : No nearby records found"
+ "Incoming dataset has an older Active Timestamp than the preferred network"
+ "Incoming dataset has no usable Active Timestamp"
+ "Incoming dataset is missing TLVs the preferred network carries"
+ "No active border router records found"
+ "No credentials stored for this border agent"
+ "No credentials stored for this extended PAN ID"
+ "No credentials stored for this unique identifier"
+ "No nearby active border router records found"
+ "Retrieved %lu stored active data set record(s) but none could be deserialized"
+ "Stored active data set records could not be deserialized"
+ "TNCKBS:Failed to fetch active dataset records for borderAgent %@:err=%@"
+ "TNCKBS:No stored record for UUID %@"
+ "TNCKBS:No stored record for borderAgent %@"
+ "extended pan id"
+ "incoming dataset drops TLVs the stored preferred network carries (dropped mask 0x%x)"
+ "incoming dataset has an older Active Timestamp than the stored preferred network"
+ "incoming dataset has no usable Active Timestamp while the stored preferred network does"
+ "isValidTLVType:length:value:availableLength:"
+ "network key"
+ "precedence check - stored{parsed:%d ts:%d/0x%llX tlv:0x%x} incoming{parsed:%d ts:%d/0x%llX tlv:0x%x}"
+ "pskc"
+ "validateDataSetStructure:"
- "%@"
- "%s : #MOS : %s Page is not Zero : %d"
- "%s : #MOS : %s is not in the range : %d"
- "%s is not in the range : %d"
- "%s: #MOS : ==> Decoded %s Len : %d"
- "%s: #MOS : ==> Decoded Channel mask, mask entry format is invalid, Line : %d"
- "%s: #MOS : ==> Invalid Mesh local prefix length %d, Line : %d"
- "%s: #MOS : ==> Invalid Security Policy length %d, Line : %d"
- "%s: #MOS : ==> Invalid extended pan id length %d, Line : %d"
- "%s: #MOS : ==> Invalid network key length %d, Line : %d"
- "%s: #MOS : ==> Invalid pan id length %d, Line : %d"
- "%s: #MOS : ==> Invalid pskc length %d, Line : %d"
- "%s: #MOS : ==> Invalid rotation time, Line : %d"
- "%s: #MOS : ==> error : Decoded Channel page is neither zero nor 2,  Line : %d"
- "%s: #MOS : ==> error : Decoded entry length is not matching,  Line : %d"
- "%s:%d: This preferred network entry has a record associated with it, record name : %@, dataset : %@, check if it is frozen or not"
- "-[THThreadNetworkCredentialsKeychainBackingStore parsedChannelFromData:len:currentPos:debugDescription:error:]"
- "-[THThreadNetworkCredentialsStoreLocalClient parsedChannelFromData:len:currentPos:debugDescription:error:]"
- "==> Decoded %s Len : %d"
- "==> Decoded Channel Mask TLV"
- "==> Decoded Channel mask, mask entry format is invalid"
- "==> Invalid Mesh local prefix length %d"
- "==> Invalid Security Policy length %d"
- "==> Invalid extended pan id length %d"
- "==> Invalid network key length %d"
- "==> Invalid pan id length %d"
- "==> Invalid pskc length %d,  "
- "==> Invalid rotation time"
- "==> error : Decoded Channel page is neither zero nor 2"
- "==> error : Decoded entry length is not matching"
- "C48@0:8r*16C24I28r*32^@40"
- "Failed to retrieve all active border router records"
- "Failed to run mdns check; Unable to parse the Active Operational Data Set"
- "parsedChannelFromData:len:currentPos:debugDescription:error:"
```
