## CoreAudioKit

> `/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit`

```diff

-279.505.0.0.0
-  __TEXT.__text: 0xef9c4
-  __TEXT.__auth_stubs: 0x2bb0
-  __TEXT.__objc_methlist: 0x3cc8
+279.506.0.0.0
+  __TEXT.__text: 0xefe34
+  __TEXT.__auth_stubs: 0x2ba0
+  __TEXT.__objc_methlist: 0x3d78
   __TEXT.__const: 0x4e9a
-  __TEXT.__gcc_except_tab: 0x140c
-  __TEXT.__cstring: 0x4b7c
+  __TEXT.__gcc_except_tab: 0x14dc
+  __TEXT.__cstring: 0x3cfc
   __TEXT.__oslogstring: 0x434
   __TEXT.__constg_swiftt: 0x4b0c
   __TEXT.__swift5_typeref: 0x15326

   __TEXT.__swift5_types: 0x1d8
   __TEXT.__swift5_capture: 0x904
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__unwind_info: 0x2898
+  __TEXT.__unwind_info: 0x28a8
   __TEXT.__eh_frame: 0xb4
-  __TEXT.__objc_classname: 0x13f2
-  __TEXT.__objc_methname: 0xa28c
-  __TEXT.__objc_methtype: 0x2980
-  __TEXT.__objc_stubs: 0x64c0
-  __DATA_CONST.__got: 0xa58
+  __TEXT.__objc_classname: 0x1407
+  __TEXT.__objc_methname: 0xa43c
+  __TEXT.__objc_methtype: 0x2a35
+  __TEXT.__objc_stubs: 0x65a0
+  __DATA_CONST.__got: 0xa60
   __DATA_CONST.__const: 0x2c8
   __DATA_CONST.__objc_classlist: 0x338
-  __DATA_CONST.__objc_protolist: 0xe0
+  __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2688
+  __DATA_CONST.__objc_selrefs: 0x2708
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x15f0
+  __AUTH_CONST.__auth_got: 0x15e8
   __AUTH_CONST.__const: 0x43a0
   __AUTH_CONST.__cfstring: 0x1b20
-  __AUTH_CONST.__objc_const: 0x85c8
+  __AUTH_CONST.__objc_const: 0x8680
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0xab90
   __AUTH.__data: 0x14d8
-  __DATA.__objc_ivar: 0x2a0
-  __DATA.__data: 0x3898
+  __DATA.__objc_ivar: 0x2a8
+  __DATA.__data: 0x38f8
   __DATA.__bss: 0x2a80
   __DATA.__common: 0x2b8
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 30FBF494-200B-3F6B-B198-D12B66666491
-  Functions: 3489
-  Symbols:   4963
-  CStrings:  2896
+  UUID: 74A5C80B-9979-32B8-91BB-51256676BFEA
+  Functions: 3496
+  Symbols:   4988
+  CStrings:  2911
 
Symbols:
+ -[NetServiceDirectory netService:didNotResolve:]
+ -[NetServiceDirectory netService:didUpdateTXTRecordData:]
+ -[NetServiceDirectory netServiceDidResolveAddress:]
+ -[RendezvousService setTxtRecord:]
+ -[RendezvousService txtRecord]
+ _OBJC_CLASS_$_NSNetService
+ _OBJC_IVAR_$_NetServiceDirectory.mResolvingServices
+ _OBJC_IVAR_$_RendezvousService._txtRecord
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSNetServiceDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSNetServiceDelegate
+ __OBJC_$_PROTOCOL_REFS_NSNetServiceDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSNetServiceDelegate
+ __OBJC_PROTOCOL_$_NSNetServiceDelegate
+ __ZNSt12length_errorC1B9nqe210106EPKc
+ __ZNSt3__110unique_ptrI19NetworkDriverRTDataNS_14default_deleteIS1_EEE5resetB9nqe210106EPS1_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__114__split_bufferINS_10unique_ptrIN19NetworkDriverRTData12LatencyEventENS_14default_deleteIS3_EEEERNS_9allocatorIS6_EEE17__destruct_at_endB9nqe210106EPS6_
+ __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIN19NetworkDriverRTData12LatencyEventEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorINS_10unique_ptrIN19NetworkDriverRTData12LatencyEventENS_14default_deleteIS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__120__throw_length_errorB9nqe210106EPKc
+ __ZNSt3__127__insertion_sort_incompleteB9nqe210106INS_17_ClassicAlgPolicyERZ43-[NetworkDriverAdapter deviceErrorsChanged]E3$_1PZ43-[NetworkDriverAdapter deviceErrorsChanged]E10ErrorEntryEEbT1_S6_T0_
+ __ZNSt3__16vectorIN19NetworkDriverRTData12LatencyEventENS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorIN19NetworkDriverRTData12LatencyEventENS_9allocatorIS2_EEE9push_backB9nqe210106ERKS2_
+ __ZNSt3__16vectorINS_10unique_ptrIN19NetworkDriverRTData12LatencyEventENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE16__destroy_vectorclB9nqe210106Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN19NetworkDriverRTData12LatencyEventENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN19NetworkDriverRTData12LatencyEventENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE22__base_destruct_at_endB9nqe210106EPS6_
+ __ZNSt3__16vectorIZ43-[NetworkDriverAdapter deviceErrorsChanged]E10ErrorEntryNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorIZ43-[NetworkDriverAdapter deviceErrorsChanged]E10ErrorEntryNS_9allocatorIS1_EEED1B9nqe210106Ev
+ __ZNSt3__17__sort3B9nqe210106INS_17_ClassicAlgPolicyERZ43-[NetworkDriverAdapter deviceErrorsChanged]E3$_1PZ43-[NetworkDriverAdapter deviceErrorsChanged]E10ErrorEntryLi0EEEbT1_S6_S6_T0_
+ __ZNSt3__17__sort5B9nqe210106INS_17_ClassicAlgPolicyERZ43-[NetworkDriverAdapter deviceErrorsChanged]E3$_1PZ43-[NetworkDriverAdapter deviceErrorsChanged]E10ErrorEntryLi0EEEvT1_S6_S6_S6_S6_T0_
+ __ZNSt3__19iter_swapB9nqe210106IPZ43-[NetworkDriverAdapter deviceErrorsChanged]E10ErrorEntryS2_EEvT_T0_
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
+ _objc_msgSend$dictionaryFromTXTRecordData:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$resolveWithTimeout:
+ _objc_msgSend$setTxtRecord:
+ _objc_msgSend$startMonitoring
+ _objc_msgSend$stopMonitoring
+ _objc_msgSend$txtRecord
- __ZNSt12length_errorC1B9foe210106EPKc
- __ZNSt3__110unique_ptrI19NetworkDriverRTDataNS_14default_deleteIS1_EEE5resetB9foe210106EPS1_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__114__split_bufferINS_10unique_ptrIN19NetworkDriverRTData12LatencyEventENS_14default_deleteIS3_EEEERNS_9allocatorIS6_EEE17__destruct_at_endB9foe210106EPS6_
- __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIN19NetworkDriverRTData12LatencyEventEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorINS_10unique_ptrIN19NetworkDriverRTData12LatencyEventENS_14default_deleteIS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__120__throw_length_errorB9foe210106EPKc
- __ZNSt3__127__insertion_sort_incompleteB9foe210106INS_17_ClassicAlgPolicyERZ43-[NetworkDriverAdapter deviceErrorsChanged]E3$_1PZ43-[NetworkDriverAdapter deviceErrorsChanged]E10ErrorEntryEEbT1_S6_T0_
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__16vectorIN19NetworkDriverRTData12LatencyEventENS_9allocatorIS2_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorIN19NetworkDriverRTData12LatencyEventENS_9allocatorIS2_EEE9push_backB9foe210106ERKS2_
- __ZNSt3__16vectorINS_10unique_ptrIN19NetworkDriverRTData12LatencyEventENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE16__destroy_vectorclB9foe210106Ev
- __ZNSt3__16vectorINS_10unique_ptrIN19NetworkDriverRTData12LatencyEventENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorINS_10unique_ptrIN19NetworkDriverRTData12LatencyEventENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE22__base_destruct_at_endB9foe210106EPS6_
- __ZNSt3__16vectorIZ43-[NetworkDriverAdapter deviceErrorsChanged]E10ErrorEntryNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorIZ43-[NetworkDriverAdapter deviceErrorsChanged]E10ErrorEntryNS_9allocatorIS1_EEED1B9foe210106Ev
- __ZNSt3__17__sort3B9foe210106INS_17_ClassicAlgPolicyERZ43-[NetworkDriverAdapter deviceErrorsChanged]E3$_1PZ43-[NetworkDriverAdapter deviceErrorsChanged]E10ErrorEntryLi0EEEbT1_S6_S6_T0_
- __ZNSt3__17__sort5B9foe210106INS_17_ClassicAlgPolicyERZ43-[NetworkDriverAdapter deviceErrorsChanged]E3$_1PZ43-[NetworkDriverAdapter deviceErrorsChanged]E10ErrorEntryLi0EEEvT1_S6_S6_S6_S6_T0_
- __ZNSt3__19iter_swapB9foe210106IPZ43-[NetworkDriverAdapter deviceErrorsChanged]E10ErrorEntryS2_EEvT_T0_
- __ZSt28__throw_bad_array_new_lengthB9foe210106v
CStrings:
+ "@\"NSDictionary\""
+ "NSNetServiceDelegate"
+ "T@\"NSDictionary\",C,N,V_txtRecord"
+ "_txtRecord"
+ "dictionaryFromTXTRecordData:"
+ "initWithData:encoding:"
+ "mResolvingServices"
+ "netService:didAcceptConnectionWithInputStream:outputStream:"
+ "netService:didNotPublish:"
+ "netService:didNotResolve:"
+ "netService:didUpdateTXTRecordData:"
+ "netServiceDidPublish:"
+ "netServiceDidResolveAddress:"
+ "netServiceDidStop:"
+ "netServiceWillPublish:"
+ "netServiceWillResolve:"
+ "resolveWithTimeout:"
+ "setTxtRecord:"
+ "startMonitoring"
+ "stopMonitoring"
+ "txtRecord"
+ "v24@0:8@\"NSNetService\"16"
+ "v32@0:8@\"NSNetService\"16@\"NSData\"24"
+ "v32@0:8@\"NSNetService\"16@\"NSDictionary\"24"
+ "v40@0:8@\"NSNetService\"16@\"NSInputStream\"24@\"NSOutputStream\"32"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugAWbVbh6kyq3AKYl8N4AY6eoAz4v8qJGV0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugAWbVbh6kyq3AKYl8N4AY6eoAz4v8qJGV0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugAWbVbh6kyq3AKYl8N4AY6eoAz4v8qJGV0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugAWbVbh6kyq3AKYl8N4AY6eoAz4v8qJGV0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugAWbVbh6kyq3AKYl8N4AY6eoAz4v8qJGV0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugAWbVbh6kyq3AKYl8N4AY6eoAz4v8qJGV0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugAWbVbh6kyq3AKYl8N4AY6eoAz4v8qJGV0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugAWbVbh6kyq3AKYl8N4AY6eoAz4v8qJGV0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugAWbVbh6kyq3AKYl8N4AY6eoAz4v8qJGV0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugAWbVbh6kyq3AKYl8N4AY6eoAz4v8qJGV0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"

```
