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

-442.0.0.0.0
-  __TEXT.__text: 0x424028
-  __TEXT.__auth_stubs: 0x12950
-  __TEXT.__objc_stubs: 0xa160
+446.0.5.0.0
+  __TEXT.__text: 0x427228
+  __TEXT.__auth_stubs: 0x12970
+  __TEXT.__objc_stubs: 0xa1e0
   __TEXT.__init_offsets: 0xb4
-  __TEXT.__objc_methlist: 0x6b3c
-  __TEXT.__gcc_except_tab: 0x2a6e4
-  __TEXT.__const: 0x8674
-  __TEXT.__oslogstring: 0x28966
-  __TEXT.__cstring: 0x37510
+  __TEXT.__objc_methlist: 0x6b7c
+  __TEXT.__gcc_except_tab: 0x2ab3c
+  __TEXT.__const: 0x86b4
+  __TEXT.__oslogstring: 0x2963b
+  __TEXT.__cstring: 0x377cd
   __TEXT.__objc_classname: 0x6eb
-  __TEXT.__objc_methname: 0xf877
-  __TEXT.__objc_methtype: 0x44d1
+  __TEXT.__objc_methname: 0xf961
+  __TEXT.__objc_methtype: 0x44e7
   __TEXT.__swift5_typeref: 0x572
   __TEXT.__swift5_capture: 0x60c
   __TEXT.__swift5_fieldmd: 0x130

   __TEXT.__swift_as_entry: 0xac
   __TEXT.__swift_as_ret: 0x88
   __TEXT.__swift_as_cont: 0x1dc
-  __TEXT.__info_plist: 0x3bf
-  __TEXT.__unwind_info: 0x149c0
+  __TEXT.__info_plist: 0x3c5
+  __TEXT.__unwind_info: 0x14a00
   __TEXT.__eh_frame: 0x1f68
   __DATA_CONST.__const: 0xddb8
-  __DATA_CONST.__cfstring: 0x6e00
+  __DATA_CONST.__cfstring: 0x6f00
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x140
-  __DATA_CONST.__auth_got: 0x94c0
+  __DATA_CONST.__auth_got: 0x94d0
   __DATA_CONST.__got: 0xbc8
   __DATA_CONST.__auth_ptr: 0x240
-  __DATA.__objc_const: 0x8b68
-  __DATA.__objc_selrefs: 0x38b0
-  __DATA.__objc_ivar: 0x558
+  __DATA.__objc_const: 0x8b98
+  __DATA.__objc_selrefs: 0x38e0
+  __DATA.__objc_ivar: 0x55c
   __DATA.__objc_data: 0x1060
   __DATA.__data: 0xa11
   __DATA.__common: 0x3eec0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 18403
-  Symbols:   24133
-  CStrings:  13532
+  Functions: 18414
+  Symbols:   24159
+  CStrings:  13608
 
Symbols:
+ -[THThreadNetworkCredentialsStoreLocalClient isValidTLVType:length:value:availableLength:]
+ -[THThreadNetworkCredentialsStoreLocalClient validateDataSetStructure:]
+ -[ThreadNetworkManagerInstance aodIntegrityPreviousCheckPending]
+ -[ThreadNetworkManagerInstance credentialTlvMaskForDataSet:]
+ -[ThreadNetworkManagerInstance dataSet:retainsTlvsOf:]
+ -[ThreadNetworkManagerInstance getActiveTimestampFromDataSet:]
+ -[ThreadNetworkManagerInstance setAodIntegrityPreviousCheckPending:]
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/CoreThreadRadio/install/Symbols/BuiltProducts/libopenthread-ftd.a(heap-6d7eecb889588d483fc188923142afb5.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/CoreThreadRadio/install/Symbols/BuiltProducts/libopenthread-ftd.a(heap-9588502b8d1baf049622c7d89b5633c0.o)
+ GCC_except_table323
+ OBJC_IVAR_$_ThreadNetworkManagerInstance._aodIntegrityPreviousCheckPending
+ THDataSetIsValidTlv
+ THIsValidChannelTlv
+ THIsValidFixedLengthTlv
+ _$s7Network9NWBrowserC10DescriptorO7OptionsV10DeviceTypeV13homeAccessoryAIvgZ
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _THDataSetIsValidTlv
+ _THIsValidChannelTlv
+ _THIsValidFixedLengthTlv
+ __117-[THThreadNetworkCredentialsKeychainBackingStore retrieveActiveDataSetRecordWithTLVsForThreadBorderAgent:completion:]_block_invoke
+ __ZN20Ctr_NCPNetworkInfo_tD1Ev
+ __ZN2ot10KeyManager8ClearKekEv
+ __ZNK2ot10KeyManager8IsKekSetEv
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
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/CoreThreadRadio/install/Symbols/BuiltProducts/libopenthread-ftd.a(heap-9d530454beb80683982d68096829ae52.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/CoreThreadRadio/install/Symbols/BuiltProducts/libopenthread-ftd.a(heap-df18cac7282a96f112bc31007f0ad181.o)
- GCC_except_table547
- _objc_msgSend$parsedChannelFromData:len:currentPos:debugDescription:error:
CStrings:
+ " %s:%d Existing preferred network has no usable Active Timestamp, preferring the NCP dataset and continuing with the update"
+ " %s:%d Incoming dataset drops Mesh-Local Prefix / PSKc / Security Policy present in the preferred network, skipping update"
+ " %s:%d Incoming dataset has no usable Active Timestamp while the existing preferred network does, skipping update"
+ " %s:%d Incoming dataset is not fresher than existing, skipping update"
+ " ActiveTimestamp"
+ " Channel"
+ " Morty_Version: V0.446.0.5"
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
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/include/c++/v1/__hash_table:1855: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/include/c++/v1/__hash_table:242: libc++ Hardening assertion __node_ != nullptr failed: Attempted to dereference a non-dereferenceable unordered container iterator\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/include/c++/v1/__hash_table:248: libc++ Hardening assertion __node_ != nullptr failed: Attempted to dereference a non-dereferenceable unordered container iterator\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/include/c++/v1/__hash_table:254: libc++ Hardening assertion __node_ != nullptr failed: Attempted to increment a non-incrementable unordered container iterator\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:47: libc++ Hardening assertion __location != nullptr failed: null pointer given to construct_at\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:59: libc++ Hardening assertion __loc != nullptr failed: null pointer given to destroy_at\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/include/c++/v1/__memory/unique_ptr.h:583: libc++ Hardening assertion __checker_.__in_bounds<deleter_type>(std::__to_address(__ptr_), __i) failed: unique_ptr<T[]>::operator[](index): index out of range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/include/c++/v1/deque:2199: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/include/c++/v1/streambuf:301: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/include/c++/v1/streambuf:302: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/include/c++/v1/streambuf:303: libc++ Hardening assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/include/c++/v1/streambuf:319: libc++ Hardening assertion std::__is_valid_range(__pbeg, __pend) failed: [pbeg, pend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/include/c++/v1/string:1074: libc++ Hardening assertion __s != nullptr failed: basic_string(const char*) detected nullptr\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/include/c++/v1/string:2219: libc++ Hardening assertion __s < __min_cap failed: __s should never be greater than or equal to the short string capacity\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/include/c++/v1/string:2226: libc++ Hardening assertion !__rep_.__s.__is_long_ failed: String has to be short when trying to get the short size\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/include/c++/v1/string:2235: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long size\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/include/c++/v1/string:2247: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long capacity\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/include/c++/v1/string:2252: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/include/c++/v1/string:2257: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
+ "/System/Library/PrivateFrameworks/CoreThreadRadio.framework/com.apple.ccmapping_macos_vendor2_cc5_ver_6_2.plist"
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
- " Morty_Version: V0.442"
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
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/include/c++/v1/__hash_table:1855: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/include/c++/v1/__hash_table:242: libc++ Hardening assertion __node_ != nullptr failed: Attempted to dereference a non-dereferenceable unordered container iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/include/c++/v1/__hash_table:248: libc++ Hardening assertion __node_ != nullptr failed: Attempted to dereference a non-dereferenceable unordered container iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/include/c++/v1/__hash_table:254: libc++ Hardening assertion __node_ != nullptr failed: Attempted to increment a non-incrementable unordered container iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:47: libc++ Hardening assertion __location != nullptr failed: null pointer given to construct_at\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:59: libc++ Hardening assertion __loc != nullptr failed: null pointer given to destroy_at\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/include/c++/v1/__memory/unique_ptr.h:583: libc++ Hardening assertion __checker_.__in_bounds<deleter_type>(std::__to_address(__ptr_), __i) failed: unique_ptr<T[]>::operator[](index): index out of range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/include/c++/v1/deque:2199: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/include/c++/v1/streambuf:301: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/include/c++/v1/streambuf:302: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/include/c++/v1/streambuf:303: libc++ Hardening assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/include/c++/v1/streambuf:319: libc++ Hardening assertion std::__is_valid_range(__pbeg, __pend) failed: [pbeg, pend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/include/c++/v1/string:1074: libc++ Hardening assertion __s != nullptr failed: basic_string(const char*) detected nullptr\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/include/c++/v1/string:2219: libc++ Hardening assertion __s < __min_cap failed: __s should never be greater than or equal to the short string capacity\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/include/c++/v1/string:2226: libc++ Hardening assertion !__rep_.__s.__is_long_ failed: String has to be short when trying to get the short size\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/include/c++/v1/string:2235: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long size\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/include/c++/v1/string:2247: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long capacity\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/include/c++/v1/string:2252: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/include/c++/v1/string:2257: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
- "/System/Library/PrivateFrameworks/CoreThreadRadio.framework/com.apple.ccmapping_macos_vendor2_cc5_ver_6_0.plist"
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
- "OT_ERROR_PARSE <<frame_unpack>>"
- "OT_ERROR_PARSE <<mac_data_unpack>>"
- "OT_ERROR_PARSE <<receiveError>>"
- "OT_ERROR_PARSE <<receiveErrorOutOfRange>>"
- "kWPANTUNDEvent_ThreadNetwork_ActiveDataSetChanged setEventHandler \n"
- "parsedChannelFromData:len:currentPos:debugDescription:error:"
```
