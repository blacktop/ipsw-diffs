## smbd

> `/usr/sbin/smbd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__dof_ntvfs`
- `__TEXT.__dof_smbd`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-676.0.0.0.0
-  __TEXT.__text: 0x7992c
+682.0.0.0.0
+  __TEXT.__text: 0x79c08
   __TEXT.__auth_stubs: 0x1f80
   __TEXT.__init_offsets: 0x14
   __TEXT.__const: 0x1287
   __TEXT.__gcc_except_tab: 0x57e0
-  __TEXT.__oslogstring: 0xa0ab
-  __TEXT.__cstring: 0xff45
+  __TEXT.__oslogstring: 0xa19f
+  __TEXT.__cstring: 0xff59
   __TEXT.__dof_ntvfs: 0x1eed
   __TEXT.__dof_smbd: 0x7aa
-  __TEXT.__unwind_info: 0x24e8
+  __TEXT.__unwind_info: 0x24f0
   __DATA_CONST.__const: 0xa8c8
   __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__auth_got: 0xfc8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libpam.2.dylib
-  Functions: 1623
-  Symbols:   2745
-  CStrings:  3192
+  Functions: 1625
+  Symbols:   2746
+  CStrings:  3197
 
Symbols:
+ __ZL19reply_buffer_appendIN4smb213lock_responseEEbR11smb_requestRKT_
Functions:
~ __ZN12smbd_service29find_reconnect_durable_handleERN5ntvfs15file_operations22lease_update_argumentsERNS1_20create_lease_resultsEP11smb_sessionbRj : 2456 -> 2764
~ __ZN11smb_session13attach_handleERN8platform11counted_ptrIN5ntvfs11file_handleEEE : 216 -> 252
~ __Z34smb2_dispatch_set_file_informationR11smb_requestPhS1_ : 2080 -> 2068
~ __Z18smb2_dispatch_lockR11smb_requestPhS1_ : 1152 -> 1028
+ __ZL20reply_buffer_reserveR11smb_requestm
~ __Z49ConvertWireSecurityDescriptorToSecurityDescriptorPKhmP20_SECURITY_DESCRIPTORm : 560 -> 556
~ __ZL21InitializeAclFromWirePKhmmRPhS1_ : 776 -> 784
~ __ZN3smb19insert_utf16_stringERK10oem_stringRPhS3_j : 940 -> 1172
~ __ZN6darwin11darwin_fileC2EiyjRKNS_11darwin_tree15fs_capabilitiesEb : 180 -> 184
~ __ZN5ntvfs11file_handleC2Ejy : 164 -> 168
~ __ZN6darwin16darwin_directoryC2EiyjbRKN5ntvfs9fsoptionsERKNS_11darwin_tree15fs_capabilitiesEb : 340 -> 348
~ __ZN6darwin11darwin_brlmC2EP7NLMDatayPKhjRKNS_11darwin_tree15fs_capabilitiesEb : 588 -> 592
~ __ZN6darwin12darwin_finfoC2EiyPKhjRKNS_11darwin_tree15fs_capabilitiesEb : 324 -> 328
~ __ZN6darwin12darwin_xattrC2EiyPKhjRKNS_11darwin_tree15fs_capabilitiesEb : 428 -> 432
+ __ZL19reply_buffer_appendIN4smb213lock_responseEEbR11smb_requestRKT_
CStrings:
+ "%s: Output buffer way too small, ndestbytes: %td"
+ "%s: numUniChars (%zu) exceeds numDestChars (%zu) for '%s'"
+ "insert_utf16_string"
+ "svc:%s: durable handle owner mismatch on dfid: 0x%llx"
+ "svc:%s: failed to obtain uid from session token, denying reconnect of dfid: 0x%llx"
```
