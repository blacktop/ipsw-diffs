## smbd

> `/usr/sbin/smbd`

```diff

-  __TEXT.__text: 0x7a344
+  __TEXT.__text: 0x7a340
   __TEXT.__auth_stubs: 0x1f80
   __TEXT.__init_offsets: 0x14
   __TEXT.__const: 0x1287
-  __TEXT.__gcc_except_tab: 0x57dc
+  __TEXT.__gcc_except_tab: 0x57e0
   __TEXT.__oslogstring: 0xa0ab
   __TEXT.__cstring: 0xff45
   __TEXT.__dof_ntvfs: 0x1eed
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__dof_ntvfs : content changed
~ __TEXT.__dof_smbd : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ __ZL21connect_to_named_treeRK11smb_requestRK10oem_stringRi : 1420 -> 1424
~ __ZNSt3__15dequeIyNS_9allocatorIyEEE19__add_back_capacityEv : 480 -> 468
~ __ZN17ntlmssp_mechanism25receive_ntlmssp_negotiateERK17ntlmssp_negotiateRN8platform11heap_bufferE : 1272 -> 1248
~ __ZL18get_create_contextRKN4smb222create_context_extractE : 144 -> 152
~ __Z29find_virtual_admin_sharepointPK10__CFStringRj : 1984 -> 1988
~ __ZN8platform13socket_writevEiP5iovecj : 420 -> 424
~ _NtGenericErrnoStatus : 64 -> 68
~ __ZL14sddl_parse_aclPcR20_SECURITY_DESCRIPTORbPP4_ACL : 1596 -> 1616
~ __ZN7secdesc7extractERPhRKS0_RNS_8WIRE_SIDES3_ : 184 -> 200
~ __ZN5ntvfs18file_control_tableC2Ej : 272 -> 292
~ __ZN6darwinL18make_relative_pathERNS_11path_bufferE : 436 -> 404
~ __ZN5ntvfs8pathname20convert_windows_pathERK10oem_stringPhS4_ : 356 -> 328
~ __ZN5ntvfs8pathname17convert_unix_pathERK10oem_stringPtS4_ : 368 -> 380
~ __ZN5ntvfs8pathname6importERK10oem_string : 1592 -> 1588
~ __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB9nqe220106IP14process_holderS5_S5_EENS_4pairIT_T1_EES7_T0_S8_ : 196 -> 200
~ __ZN5ntvfs6detail16fileid_allocator15bitmap_allocateEv : 568 -> 576
~ __ZN6darwin16follow_directoryERKN5ntvfs9fsoptionsEPKhb : 384 -> 376

```
