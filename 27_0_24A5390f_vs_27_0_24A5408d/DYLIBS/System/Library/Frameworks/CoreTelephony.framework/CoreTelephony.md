## CoreTelephony

> `/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_reflstr`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_assocty`
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
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-13482.1.0.0.0
-  __TEXT.__text: 0x1d3220
-  __TEXT.__objc_methlist: 0x1faac
+13487.3.0.0.0
+  __TEXT.__text: 0x1d38d4
+  __TEXT.__objc_methlist: 0x1facc
   __TEXT.__const: 0x1736
-  __TEXT.__gcc_except_tab: 0x258a0
+  __TEXT.__gcc_except_tab: 0x25910
   __TEXT.__cstring: 0x21fe8
   __TEXT.__oslogstring: 0x54c6
   __TEXT.__swift5_typeref: 0x2b4

   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_reflstr: 0x142
-  __TEXT.__swift5_fieldmd: 0x168
+  __TEXT.__swift5_fieldmd: 0x15c
   __TEXT.__swift5_types: 0x20
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_proto: 0x30
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x30
-  __TEXT.__unwind_info: 0x10fd8
+  __TEXT.__unwind_info: 0x11020
   __TEXT.__eh_frame: 0x370
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x288
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x88b8
+  __DATA_CONST.__objc_selrefs: 0x88c0
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x1d58
   __DATA_CONST.__objc_arraydata: 0x30

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 13084
-  Symbols:   27472
+  Functions: 13094
+  Symbols:   27482
   CStrings:  6527
 
Symbols:
+ -[CTQuickSwitchInfo .cxx_destruct]
+ -[CoreTelephonyClient(QuickSwitch) isQuickSwitchPendingTwinningWithError:]
+ __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEyEEPvEEEEEclB9fqn220106EPSB_
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEyEENS_19__map_value_compareIS7_NS_4pairIKS7_yEENS_4lessIS7_EEEENS5_ISC_EEE14__tree_deleterclB9fqn220106EPNS_11__tree_nodeIS8_PvEE
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEyEENS_19__map_value_compareIS7_NS_4pairIKS7_yEENS_4lessIS7_EEEENS5_ISC_EEE16__construct_nodeIJRKSC_EEENS_10unique_ptrINS_11__tree_nodeIS8_PvEENS_22__tree_node_destructorINS5_ISO_EEEEEEDpOT_
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEyEENS_19__map_value_compareIS7_NS_4pairIKS7_yEENS_4lessIS7_EEEENS5_ISC_EEE18__assign_from_treeB9fqn220106IZNSH_18__copy_assign_treeB9fqn220106EPNS_11__tree_nodeIS8_PvEESM_EUlRSC_RKSC_E_ZNSH_18__copy_assign_treeB9fqn220106ESM_SM_EUlSM_E_EESM_SM_SM_T_T0_
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEyEENS_19__map_value_compareIS7_NS_4pairIKS7_yEENS_4lessIS7_EEEENS5_ISC_EEE21__construct_from_treeB9fqn220106IZNSH_21__copy_construct_treeB9fqn220106EPNS_11__tree_nodeIS8_PvEEEUlRKSC_E_EESM_SM_T_
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEyEENS_19__map_value_compareIS7_NS_4pairIKS7_yEENS_4lessIS7_EEEENS5_ISC_EEEaSERKSH_
+ ___74-[CoreTelephonyClient(QuickSwitch) isQuickSwitchPendingTwinningWithError:]_block_invoke
+ ___74-[CoreTelephonyClient(QuickSwitch) isQuickSwitchPendingTwinningWithError:]_block_invoke_2
CStrings:
+ "13487.3"
+ "13487.3~40"
+ "IPHONE_HANDOFF"
- "13482.1"
- "13482.1~1"
- "AUTOMATIC_NUMBER_SWITCHING"
```
