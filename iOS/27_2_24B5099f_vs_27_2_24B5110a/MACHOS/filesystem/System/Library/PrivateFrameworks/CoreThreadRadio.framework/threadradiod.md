## threadradiod

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
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
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-446.0.2.0.1
-  __TEXT.__text: 0x41813c
-  __TEXT.__auth_stubs: 0x12be0
-  __TEXT.__objc_stubs: 0xa100
+446.0.4.0.0
+  __TEXT.__text: 0x41b030
+  __TEXT.__auth_stubs: 0x12bf0
+  __TEXT.__objc_stubs: 0xa180
   __TEXT.__init_offsets: 0xb4
-  __TEXT.__objc_methlist: 0x6aa4
-  __TEXT.__gcc_except_tab: 0x2a39c
-  __TEXT.__const: 0x8664
-  __TEXT.__oslogstring: 0x28004
-  __TEXT.__cstring: 0x371d9
+  __TEXT.__objc_methlist: 0x6ae4
+  __TEXT.__gcc_except_tab: 0x2a7f0
+  __TEXT.__const: 0x86a4
+  __TEXT.__oslogstring: 0x28cd9
+  __TEXT.__cstring: 0x37523
   __TEXT.__objc_classname: 0x6eb
-  __TEXT.__objc_methname: 0xf7d7
-  __TEXT.__objc_methtype: 0x4451
+  __TEXT.__objc_methname: 0xf8d1
+  __TEXT.__objc_methtype: 0x4467
   __TEXT.__swift5_typeref: 0x572
   __TEXT.__swift5_capture: 0x60c
   __TEXT.__swift5_fieldmd: 0x130

   __TEXT.__swift_as_entry: 0xac
   __TEXT.__swift_as_ret: 0x88
   __TEXT.__swift_as_cont: 0x1dc
-  __TEXT.__unwind_info: 0x147e0
+  __TEXT.__unwind_info: 0x14818
   __TEXT.__eh_frame: 0x1f68
   __DATA_CONST.__const: 0xdcc8
-  __DATA_CONST.__cfstring: 0x6ce0
+  __DATA_CONST.__cfstring: 0x6de0
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x140
-  __DATA_CONST.__auth_got: 0x9608
+  __DATA_CONST.__auth_got: 0x9610
   __DATA_CONST.__got: 0xbc0
   __DATA_CONST.__auth_ptr: 0x240
-  __DATA.__objc_const: 0x8b38
-  __DATA.__objc_selrefs: 0x3890
-  __DATA.__objc_ivar: 0x558
+  __DATA.__objc_const: 0x8b68
+  __DATA.__objc_selrefs: 0x38c0
+  __DATA.__objc_ivar: 0x55c
   __DATA.__objc_data: 0x1060
   __DATA.__data: 0xa39
   __DATA.__common: 0x3eec0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 18298
-  Symbols:   24097
-  CStrings:  13485
+  Functions: 18306
+  Symbols:   24118
+  CStrings:  13565
 
Symbols:
+ -[THThreadNetworkCredentialsStoreLocalClient isValidTLVType:length:value:availableLength:]
+ -[THThreadNetworkCredentialsStoreLocalClient validateDataSetStructure:]
+ -[ThreadNetworkManagerInstance aodIntegrityPreviousCheckPending]
+ -[ThreadNetworkManagerInstance credentialTlvMaskForDataSet:]
+ -[ThreadNetworkManagerInstance dataSet:retainsTlvsOf:]
+ -[ThreadNetworkManagerInstance getActiveTimestampFromDataSet:]
+ -[ThreadNetworkManagerInstance setAodIntegrityPreviousCheckPending:]
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreThreadRadio/install/Symbols/BuiltProducts/libopenthread-ftd.a(heap-d30952d653dd74fad6edeb8b2e4094ce.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreThreadRadio/install/Symbols/BuiltProducts/libopenthread-ftd.a(heap-e223533038f5bcbad4bed7ec950f4fe5.o)
+ GCC_except_table343
+ OBJC_IVAR_$_ThreadNetworkManagerInstance._aodIntegrityPreviousCheckPending
+ THDataSetIsValidTlv
+ THIsValidChannelTlv
+ THIsValidFixedLengthTlv
+ _$s7Network9NWBrowserC10DescriptorO7OptionsV10DeviceTypeV13homeAccessoryAIvgZ
+ _OUTLINED_FUNCTION_38
+ _THDataSetIsValidTlv
+ _THIsValidChannelTlv
+ _THIsValidFixedLengthTlv
+ __117-[THThreadNetworkCredentialsKeychainBackingStore retrieveActiveDataSetRecordWithTLVsForThreadBorderAgent:completion:]_block_invoke
+ __ZN20Ctr_NCPNetworkInfo_tD1Ev
+ ___150-[THThreadNetworkCredentialsStoreLocalClient storeThreadNetworkCredentialActiveDataSet:network:credentials:credentialsDataSet:waitForSync:completion:]_block_invoke_3
+ _objc_msgSend$credentialTlvMaskForDataSet:
+ _objc_msgSend$dataSet:retainsTlvsOf:
+ _objc_msgSend$getActiveTimestampFromDataSet:
+ _objc_msgSend$isValidTLVType:length:value:availableLength:
+ _objc_msgSend$validateDataSetStructure:
+ _thInspectDataSet
+ thInspectDataSet
- -[THThreadNetworkCredentialsKeychainBackingStore parsedChannelFromData:len:currentPos:debugDescription:error:]
- -[THThreadNetworkCredentialsStoreLocalClient parsedChannelFromData:len:currentPos:debugDescription:error:]
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreThreadRadio/install/Symbols/BuiltProducts/libopenthread-ftd.a(heap-5687e8b34846f6e0748af363438a87f4.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreThreadRadio/install/Symbols/BuiltProducts/libopenthread-ftd.a(heap-f5cfc0fb38c4ba27d8ae3be5b3f30d8c.o)
- GCC_except_table307
- GCC_except_table323
- GCC_except_table547
- _objc_msgSend$parsedChannelFromData:len:currentPos:debugDescription:error:
CStrings:
+ " %s:%d Existing preferred network has no usable Active Timestamp, preferring the NCP dataset and continuing with the update"
+ " %s:%d Incoming dataset drops Mesh-Local Prefix / PSKc / Security Policy present in the preferred network, skipping update"
+ " %s:%d Incoming dataset has no usable Active Timestamp while the existing preferred network does, skipping update"
+ " %s:%d Incoming dataset is not fresher than existing, skipping update"
+ " ActiveTimestamp"
+ " Channel"
+ " Morty_Version: V0.446.0.4"
+ " NetworkKey"
+ " NetworkName"
+ " PANID"
+ " XPANID"
+ "%s : %d : creds_active_timestamp : 0x%llX (%lld), cfg_active_timestamp : 0x%llX"
+ "%s : %d : creds_dataSetArray : %{sensitive}s"
+ "%s : %d : creds_ml_prefix : %@, cfg_ml_prefix : %s"
+ "%s : %d : incoming_active_timestamp : 0x%llX (%lld), existing_active_timestamp : 0x%llX (%lld)"
+ "%s : %d : incoming_dataSetArray : %{sensitive}s"
+ "%s : %d : lastKnownJoined_dataSetArray : %{sensitive}s"
+ "%s : %d : ncp_dataSetArray : %{sensitive}s"
+ "%s : %d : preferred_dataSetArray : %{sensitive}s"
+ "%s : %s arrived as unexpected type \"%s\" (non-fatal)"
+ "%s : Active Timestamp: %llu"
+ "%s : Failed to get %s (non-fatal) = %s, Error Info: %s"
+ "%s : ML Prefix: %s"
+ "%s: #MOS : ==> Dataset is nil or empty, Line : %d"
+ "%s: #MOS : ==> Decoded TLV, format is invalid, cannot read length, Line : %d"
+ "%s: #MOS : ==> Duplicate type is detected : %d, Line : %d"
+ "%s: #MOS : ==> Invalid dataset length %d, max is %d, Line : %d"
+ "%s: #MOS : ==> Invalid dataset length %lu, max is %d, Line : %d"
+ "%s: #MOS : Channel Mask : %@"
+ "%s: #MOS : Mesh Local Prefix : %@"
+ "%s: #MOS : Security Policy : %@"
+ "%s: %d: Dataset carries no PSKc; accepting it, since PSKc is only needed to authenticate an external commissioner"
+ "%s: %d: Rejecting dataset, missing required TLVs:%s%s%s%s%s%s"
+ "%s: %d: Warning : dataset is incomplete : ml_prefix : %@, sec_policy : %@, channel_mask : %@"
+ "%s: Active Timestamp TLV holds OpenThread's invalid encoding (all ones), treating as absent"
+ "%s:%d: Active Timestamp TLV holds OpenThread's invalid encoding (all ones), reporting as no usable timestamp"
+ "%s:%d: Incoming record supersedes the preferred network, allowing the store"
+ "%s:%d: Preferred network %s, upgrading it from the NCP's dataset"
+ "%s:%d: Preferred network already carries a dataset (%lu bytes), nothing to upgrade"
+ "%s:%d: Rejecting store - %{public}@"
+ "%s:%d: This preferred network entry has a record associated with it, record name : %@, dataset length : %lu, dataset : %{sensitive}s, check if it is frozen or not"
+ "%s:%d: incoming TLV mask 0x%x would drop 0x%x from stored mask 0x%x"
+ "%s:%d: precedence check skipped - dataset could not be parsed (stored:%d incoming:%d)"
+ "(empty)"
+ "-[THThreadNetworkCredentialsKeychainBackingStore areValidDataSetTLVs:creds:updateATS:isATSAppended:]"
+ "-[THThreadNetworkCredentialsStoreLocalClient validateDataSetStructure:]"
+ "-[ThreadNetworkManagerInstance dataSet:retainsTlvsOf:]"
+ "-[ThreadNetworkManagerInstance getActiveTimestampFromDataSet:]"
+ "==> Invalid dataset length %d, max is %d"
+ "Active Operational Dataset is invalid or incomplete"
+ "Active Timestamp TLV not present in Active Dataset"
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
+ "HI:PG0:%s: Active Timestamp TLV holds the invalid encoding (all ones), reporting as absent"
+ "HI:PG0:%s: truncated TLV at offset %u (type %u len %u, dataset len %u)"
+ "HI:PG0:%s=0x%016llX (seconds=%llu ticks=%u authoritative=%d)"
+ "HI:PG0:%s=Active Timestamp TLV not present in Active Dataset"
+ "I24@0:8@16"
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
+ "TB,V_aodIntegrityPreviousCheckPending"
+ "TNCKBS:Failed to fetch active dataset records for borderAgent %@:err=%@"
+ "TNCKBS:No stored record for UUID %@"
+ "TNCKBS:No stored record for borderAgent %@"
+ "TNM:Checking for Preferred network availability to join"
+ "TNM:Checking to see if already on preferred network or not from check preferred timer handler"
+ "TNM:PeriodicCaCollectionMeshcop is Running , So skipping checkPreferredThreadNetworkTimerHandler functionality"
+ "TNM:check preferred thread network timer handler"
+ "TNM:check preferred thread network timer handler Done"
+ "_aodIntegrityPreviousCheckPending"
+ "aodIntegrityPreviousCheckPending"
+ "carries no dataset (pre-TLV format)"
+ "credentialTlvMaskForDataSet:"
+ "dataSet:retainsTlvsOf:"
+ "extended pan id"
+ "getActiveTimestampFromDataSet:"
+ "incoming dataset drops TLVs the stored preferred network carries (dropped mask 0x%x)"
+ "incoming dataset has an older Active Timestamp than the stored preferred network"
+ "incoming dataset has no usable Active Timestamp while the stored preferred network does"
+ "isValidTLVType:length:value:availableLength:"
+ "kWPANTUNDEvent_ThreadNetwork_ActiveDataSetChanged setEventHandler in state %s \n"
+ "network key"
+ "not found"
+ "precedence check - stored{parsed:%d ts:%d/0x%llX tlv:0x%x} incoming{parsed:%d ts:%d/0x%llX tlv:0x%x}"
+ "q24@0:8@16"
+ "setAodIntegrityPreviousCheckPending:"
+ "validateDataSetStructure:"
- " Morty_Version: V0.446.0.3"
- "%s : #MOS : %s Page is not Zero : %d"
- "%s : #MOS : %s is not in the range : %d"
- "%s is not in the range : %d"
- "%s: #MOS : ==> Decoded %s Len : %d"
- "%s: %d: Can not parse dataset tlvs"
- "%s:%d: Checking for Preferred network availability to join"
- "%s:%d: Checking to see if already on preferred network or not from check preferred timer handler"
- "%s:%d: PeriodicCaCollectionMeshcop is Running , So skipping checkPreferredThreadNetworkTimerHandler functionality"
- "%s:%d: This preferred network entry has a record associated with it, record name : %@, dataset : %@, check if it is frozen or not"
- "%s:%d: check preferred thread network timer handler"
- "%s:%d: check preferred thread network timer handler Done"
- "-[THThreadNetworkCredentialsKeychainBackingStore parsedChannelFromData:len:currentPos:debugDescription:error:]"
- "-[THThreadNetworkCredentialsStoreLocalClient parsedChannelFromData:len:currentPos:debugDescription:error:]"
- "-[ThreadNetworkManagerInstance checkPreferredThreadNetworkTimerHandler]"
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
- "kWPANTUNDEvent_ThreadNetwork_ActiveDataSetChanged setEventHandler \n"
- "parsedChannelFromData:len:currentPos:debugDescription:error:"
```
