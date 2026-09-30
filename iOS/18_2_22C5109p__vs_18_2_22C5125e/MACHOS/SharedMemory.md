## SharedMemory

> `/System/ExclaveKit/System/Library/Frameworks/SharedMemory.framework/SharedMemory`

```diff

-40.60.7.0.0
-  __TEXT.__text: 0x104cc
+40.60.8.0.0
+  __TEXT.__text: 0x1070c
   __TEXT.__auth_stubs: 0x570
   __TEXT.__const: 0x518
-  __TEXT.__cstring: 0x3ae1
+  __TEXT.__cstring: 0x3621
   __TEXT.__swift5_typeref: 0x1f6
   __TEXT.__swift5_capture: 0x20
   __TEXT.__constg_swiftt: 0x4bc

   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0x38
   __TEXT.__swift5_types: 0x70
-  __TEXT.__unwind_info: 0x4a0
+  __TEXT.__unwind_info: 0x4a8
   __TEXT.__eh_frame: 0x308
   __DATA.__auth_got: 0x2b8
   __DATA.__got: 0x50
   __DATA.__auth_ptr: 0x40
-  __DATA.__const: 0x1408
+  __DATA.__const: 0x1418
   __DATA.__objc_classlist: 0x20
   __DATA.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x340

   - /System/ExclaveKit/usr/lib/swift/libswift_errno.dylib
   - /System/ExclaveKit/usr/lib/swift/libswift_stdio.dylib
   - /System/ExclaveKit/usr/lib/swift/libswift_time.dylib
-  Functions: 501
-  Symbols:   1067
-  CStrings:  214
+  Functions: 497
+  Symbols:   1064
+  CStrings:  207
 
Symbols:
+ __block_descriptor_tmp.102
+ __block_descriptor_tmp.109
+ __block_descriptor_tmp.116
+ __block_descriptor_tmp.123
+ __block_descriptor_tmp.124
+ __block_descriptor_tmp.130
+ __block_descriptor_tmp.136
+ __block_descriptor_tmp.139
+ __block_descriptor_tmp.143
+ __block_descriptor_tmp.144
+ __block_descriptor_tmp.147
+ __block_descriptor_tmp.158
+ __block_descriptor_tmp.16
+ __block_descriptor_tmp.162
+ __block_descriptor_tmp.164
+ __block_descriptor_tmp.28
+ __block_descriptor_tmp.54
+ __block_descriptor_tmp.65
+ __block_descriptor_tmp.72
+ __block_descriptor_tmp.79
+ __block_descriptor_tmp.87
+ __block_descriptor_tmp.95
+ __physicaladdress__v_encode_block_invoke.163
+ __sharedmemory_segaccess__server_start_owned_block_invoke.105
+ __sharedmemory_segaccess__server_start_owned_block_invoke.105.cold.1
+ __sharedmemory_segaccess__server_start_owned_block_invoke.105.cold.2
+ __sharedmemory_segaccess__server_start_owned_block_invoke.112
+ __sharedmemory_segaccess__server_start_owned_block_invoke.112.cold.1
+ __sharedmemory_segaccess__server_start_owned_block_invoke.119
+ __sharedmemory_segaccess__server_start_owned_block_invoke.119.cold.1
+ __sharedmemory_segaccess__server_start_owned_block_invoke.61
+ __sharedmemory_segaccess__server_start_owned_block_invoke.61.cold.1
+ __sharedmemory_segaccess__server_start_owned_block_invoke.68
+ __sharedmemory_segaccess__server_start_owned_block_invoke.68.cold.1
+ __sharedmemory_segaccess__server_start_owned_block_invoke.68.cold.2
+ __sharedmemory_segaccess__server_start_owned_block_invoke.75
+ __sharedmemory_segaccess__server_start_owned_block_invoke.75.cold.1
+ __sharedmemory_segaccess__server_start_owned_block_invoke.83
+ __sharedmemory_segaccess__server_start_owned_block_invoke.83.cold.1
+ __sharedmemory_segaccess__server_start_owned_block_invoke.91
+ __sharedmemory_segaccess__server_start_owned_block_invoke.91.cold.1
+ __sharedmemory_segaccess__server_start_owned_block_invoke.98
+ __sharedmemory_segaccess__server_start_owned_block_invoke.98.cold.1
+ __sharedmemory_segbacking__server_start_owned_block_invoke.24
+ __sharedmemory_segbacking__server_start_owned_block_invoke.24.cold.1
+ __sharedmemory_segbacking__server_start_owned_block_invoke.32
+ __sharedmemory_segbacking__server_start_owned_block_invoke.32.cold.1
+ __sharedmemorybase_pagerange__v_encode_block_invoke.140
+ _sharedmemorybase_accessstatus__encode
+ _sharedmemorybase_mappinginfo__encode
+ _sharedmemorybase_parameters__encode
- __block_descriptor_tmp.113
- __block_descriptor_tmp.114
- __block_descriptor_tmp.120
- __block_descriptor_tmp.121
- __block_descriptor_tmp.126
- __block_descriptor_tmp.129
- __block_descriptor_tmp.13
- __block_descriptor_tmp.132
- __block_descriptor_tmp.149
- __block_descriptor_tmp.168
- __block_descriptor_tmp.173
- __block_descriptor_tmp.175
- __block_descriptor_tmp.33
- __block_descriptor_tmp.45
- __block_descriptor_tmp.55
- __block_descriptor_tmp.62
- __block_descriptor_tmp.69
- __block_descriptor_tmp.77
- __block_descriptor_tmp.85
- __block_descriptor_tmp.92
- __block_descriptor_tmp.99
- __physicaladdress__v_encode_block_invoke.174
- __sharedmemory_segaccess__server_start_owned_block_invoke.102
- __sharedmemory_segaccess__server_start_owned_block_invoke.102.cold.1
- __sharedmemory_segaccess__server_start_owned_block_invoke.109
- __sharedmemory_segaccess__server_start_owned_block_invoke.109.cold.1
- __sharedmemory_segaccess__server_start_owned_block_invoke.51
- __sharedmemory_segaccess__server_start_owned_block_invoke.51.cold.1
- __sharedmemory_segaccess__server_start_owned_block_invoke.58
- __sharedmemory_segaccess__server_start_owned_block_invoke.58.cold.1
- __sharedmemory_segaccess__server_start_owned_block_invoke.65
- __sharedmemory_segaccess__server_start_owned_block_invoke.65.cold.1
- __sharedmemory_segaccess__server_start_owned_block_invoke.73
- __sharedmemory_segaccess__server_start_owned_block_invoke.73.cold.1
- __sharedmemory_segaccess__server_start_owned_block_invoke.81
- __sharedmemory_segaccess__server_start_owned_block_invoke.81.cold.1
- __sharedmemory_segaccess__server_start_owned_block_invoke.88
- __sharedmemory_segaccess__server_start_owned_block_invoke.88.cold.1
- __sharedmemory_segaccess__server_start_owned_block_invoke.95
- __sharedmemory_segaccess__server_start_owned_block_invoke.95.cold.1
- __sharedmemory_segaccess__server_start_owned_block_invoke.cold.31
- __sharedmemory_segbacking__server_start_owned_block_invoke.21
- __sharedmemory_segbacking__server_start_owned_block_invoke.21.cold.1
- __sharedmemory_segbacking__server_start_owned_block_invoke.29
- __sharedmemory_segbacking__server_start_owned_block_invoke.29.cold.1
- __sharedmemorybase_pagerange__v_encode_block_invoke.130
- _sharedmemorybase_status__encode
- sharedmemory_segaccess_createmapping.cold.1
- sharedmemory_segaccess_mappinggetframe.cold.1
- sharedmemory_segaccess_mappinggetinfo.cold.1
- sharedmemory_segaccess_mappingmap.cold.1
- sharedmemory_segaccess_mappingsetmapped.cold.1
- sharedmemory_segaccess_mappingunmap.cold.1
CStrings:
+ "TB_FATAL: invalid error returned from backRange (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from createMapping (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from mappingDestroy (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from mappingGetFrame (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from mappingGetInfo (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from mappingGetPhysicalAddress (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from mappingGetPhysicalAddresses (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from mappingMap (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from mappingSetMapped (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from mappingUnmap (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from unbackRange (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid value: unexpected case value, %!l(MISSING)lx (%!s(MISSING):%!d(MISSING))\n"
+ "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[40c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
- "(decode_error == TB_ERROR_SUCCESS) && \"tb_message_decode_capability failed\""
- "(physicaladdress__v_decode(message, &result->value.success) == TB_ERROR_SUCCESS) && \"failed to decode type: SharedMemoryBase.PhysicalAddress (aka. UInt64)\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from backRange\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from createMapping\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from mappingDestroy\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from mappingGetFrame\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from mappingGetInfo\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from mappingGetPhysicalAddress\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from mappingGetPhysicalAddresses\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from mappingMap\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from mappingSetMapped\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from mappingUnmap\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from unbackRange\""
- "(sharedmemory_backingerror__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: SharedMemory.BackingError\""
- "(sharedmemorybase_accesserror__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: SharedMemoryBase.AccessError\""
- "(sharedmemorybase_mappinginfo__decode(message, &result->value.success) == TB_ERROR_SUCCESS) && \"failed to decode type: SharedMemoryBase.MappingInfo\""
- "(sharedmemorybase_mappingresult__decode(message, &result->value.success) == TB_ERROR_SUCCESS) && \"failed to decode type: SharedMemoryBase.MappingResult\""
- "(sharedmemorybase_perms__decode(message, &opt->value) == TB_ERROR_SUCCESS) && \"failed to decode type: SharedMemoryBase.Perms\""
- "(sharedmemorybase_perms__decode(msg, &perm) == TB_ERROR_SUCCESS) && \"failed to decode type: SharedMemoryBase.Perms\""
- "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[32c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"

```
