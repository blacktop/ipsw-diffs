## DesktopServicesPriv

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesPriv`

```diff

-1827.1.10.0.0
-  __TEXT.__text: 0x1184dc
+1827.1.12.0.0
+  __TEXT.__text: 0x1195f8
   __TEXT.__auth_stubs: 0x1e90
-  __TEXT.__objc_methlist: 0x3604
+  __TEXT.__objc_methlist: 0x366c
   __TEXT.__const: 0x4b08
-  __TEXT.__gcc_except_tab: 0x1bb90
+  __TEXT.__gcc_except_tab: 0x1be10
   __TEXT.__oslogstring: 0x345b
-  __TEXT.__cstring: 0x45cb
+  __TEXT.__cstring: 0x46e1
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0x8740
+  __TEXT.__unwind_info: 0x87c0
   __TEXT.__objc_classname: 0x859
-  __TEXT.__objc_methname: 0x7b4d
-  __TEXT.__objc_methtype: 0x5f1c
-  __TEXT.__objc_stubs: 0x61a0
+  __TEXT.__objc_methname: 0x7b7f
+  __TEXT.__objc_methtype: 0x5fbe
+  __TEXT.__objc_stubs: 0x6200
   __DATA_CONST.__got: 0xa08
   __DATA_CONST.__const: 0xb60
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2078
+  __DATA_CONST.__objc_selrefs: 0x2090
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x88
   __AUTH_CONST.__auth_got: 0xf60
   __AUTH_CONST.__const: 0x5c00
-  __AUTH_CONST.__cfstring: 0x1aa0
+  __AUTH_CONST.__cfstring: 0x1b80
   __AUTH_CONST.__objc_const: 0x60b0
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D3DAB51D-74A3-3EA5-BA9E-A9249E06D862
-  Functions: 5416
-  Symbols:   17199
-  CStrings:  3103
+  UUID: 6B1D4EE5-3D9A-3FC7-8744-69E85CC3ACEA
+  Functions: 5426
+  Symbols:   17233
+  CStrings:  3138
 
Symbols:
+ -[FIDSNode longDescription]
+ -[FIDSNode sanitizedName]
+ -[FIDSNode sanitizedURLOrPath]
+ -[FIDSNode_FPProvider longDescription]
+ -[FIDSNode_FPProvider shortDescription]
+ -[FIDSNode_FPv2 longDescription]
+ -[FINode _longDescription]
+ -[FINode description]
+ -[FINode sanitizedName]
+ -[FIProxyNode longDescription]
+ _objc_msgSend$_longDescription
+ _objc_msgSend$sanitizedName
+ _objc_msgSend$sanitizedURLOrPath
CStrings:
+ " %@"
+ "%@ - %@"
+ "%@ - %@, fsParent: %p"
+ "%@ {raw: '%@'}"
+ "'%@'"
+ ",\n\t FPItem: `%@`"
+ ", FPItem ID: %@"
+ ", FPItem ID: `%@`"
+ ", FPProviderDomain ID: `%@`"
+ ", FPProviderDomain: `%@`"
+ "<%@: (%@)>"
+ "AppleInternal"
+ "Developer"
+ "LiveFiles"
+ "MobileSoftwareUpdate"
+ "Servers"
+ "_longDescription"
+ "baseband_data"
+ "bin"
+ "com.apple."
+ "cores"
+ "dev"
+ "etc"
+ "hardware"
+ "local"
+ "preboot"
+ "sanitizedName"
+ "sanitizedURLOrPath"
+ "sbin"
+ "tmp"
+ "usr"
+ "wireless"
+ "xarts"
+ "{TPrivateNodeInstantiationEnabler=\"fVolumeInfoPtr\"{shared_ptr<TFSVolumeInfo>=\"__ptr_\"^{TFSVolumeInfo}\"__cntrl_\"^{__shared_weak_count}}\"fFSInfo\"{shared_ptr<TFSInfo>=\"__ptr_\"^{TFSInfo}\"__cntrl_\"^{__shared_weak_count}}\"fAliasTarget\"{TNodePtr=\"fFINode\"@\"FINode\"}\"fOperationLock\"{unique_ptr<TOperationLock, std::default_delete<TOperationLock>>=\"\"{?=\"__ptr_\"^{TOperationLock}}}\"fParent\"^{TNode}\"fChildrenList\"{unique_ptr<TChildrenList, std::default_delete<TChildrenList>>=\"\"{?=\"__ptr_\"^{TChildrenList}}}\"fCustomNode\"^v\"fNotifierList\"{unique_ptr<TNotifierList, std::default_delete<TNotifierList>>=\"\"{?=\"__ptr_\"^{TNotifierList}}}\"fOpenSyncSignpost\"{unique_ptr<AutoSignpostInterval_General_OpenSync, std::default_delete<AutoSignpostInterval_General_OpenSync>>=\"\"{?=\"__ptr_\"^{AutoSignpostInterval_General_OpenSync}}}\"fFlags\"{atomic<unsigned short>=\"__a_\"{__cxx_atomic_impl<unsigned short, std::__cxx_atomic_base_impl<unsigned short>>=\"__a_value\"AS}}}"
+ "{unique_ptr<AutoSignpostInterval_FPProvider_Gathering, std::default_delete<AutoSignpostInterval_FPProvider_Gathering>>=\"\"{?=\"__ptr_\"^{AutoSignpostInterval_FPProvider_Gathering}}}"
+ "{unordered_map<NSProgress *, TKeyValueObserver, std::hash<NSProgress *>, std::equal_to<NSProgress *>, std::allocator<std::pair<NSProgress *const, TKeyValueObserver>>>=\"__table_\"{__hash_table<std::__hash_value_type<NSProgress *, TKeyValueObserver>, std::__unordered_map_hasher<NSProgress *, std::__hash_value_type<NSProgress *, TKeyValueObserver>, std::hash<NSProgress *>, std::equal_to<NSProgress *>>, std::__unordered_map_equal<NSProgress *, std::__hash_value_type<NSProgress *, TKeyValueObserver>, std::equal_to<NSProgress *>, std::hash<NSProgress *>>, std::allocator<std::__hash_value_type<NSProgress *, TKeyValueObserver>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{unordered_map<NSURL *, std::pair<NSProgress *, TNSWeakPtr<FINode>>, std::hash<NSURL *>, std::equal_to<NSURL *>, std::allocator<std::pair<NSURL *const, std::pair<NSProgress *, TNSWeakPtr<FINode>>>>>=\"__table_\"{__hash_table<std::__hash_value_type<NSURL *, std::pair<NSProgress *, TNSWeakPtr<FINode>>>, std::__unordered_map_hasher<NSURL *, std::__hash_value_type<NSURL *, std::pair<NSProgress *, TNSWeakPtr<FINode>>>, std::hash<NSURL *>, std::equal_to<NSURL *>>, std::__unordered_map_equal<NSURL *, std::__hash_value_type<NSURL *, std::pair<NSProgress *, TNSWeakPtr<FINode>>>, std::equal_to<NSURL *>, std::hash<NSURL *>>, std::allocator<std::__hash_value_type<NSURL *, std::pair<NSProgress *, TNSWeakPtr<FINode>>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSURL *, std::pair<NSProgress *, TNSWeakPtr<FINode>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSURL *, std::pair<NSProgress *, TNSWeakPtr<FINode>>>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSURL *, std::pair<NSProgress *, TNSWeakPtr<FINode>>>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<NSURL *, std::pair<NSProgress *, TNSWeakPtr<FINode>>>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{unordered_set<FINode *, std::hash<FINode *>, std::equal_to<FINode *>, std::allocator<FINode *>>=\"__table_\"{__hash_table<FINode *, std::hash<FINode *>, std::equal_to<FINode *>, std::allocator<FINode *>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<FINode *, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<FINode *, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<FINode *, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<FINode *, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{unordered_set<NSObject *__unsafe_unretained, std::hash<NSObject *__unsafe_unretained>, std::equal_to<NSObject *__unsafe_unretained>, std::allocator<NSObject *__unsafe_unretained>>=\"__table_\"{__hash_table<NSObject *__unsafe_unretained, std::hash<NSObject *__unsafe_unretained>, std::equal_to<NSObject *__unsafe_unretained>, std::allocator<NSObject *__unsafe_unretained>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<NSObject *__unsafe_unretained, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<NSObject *__unsafe_unretained, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<NSObject *__unsafe_unretained, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<NSObject *__unsafe_unretained, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q\"__hasher_\"{hash<NSObject *__unsafe_unretained>=\"fHash\"{hash<NSObject *>=}}}\"\"{?=\"__max_load_factor_\"f\"__key_eq_\"{equal_to<NSObject *__unsafe_unretained>=\"fEqual\"{equal_to<NSObject *>=}}}}}"
+ "{vector<NSObject<FINodeIterator> *, std::allocator<NSObject<FINodeIterator> *>>=\"__begin_\"^@\"__end_\"^@\"\"{?=\"__cap_\"^@}}"
+ "{vector<TKeyValueObserver, std::allocator<TKeyValueObserver>>=\"__begin_\"^{TKeyValueObserver}\"__end_\"^{TKeyValueObserver}\"\"{?=\"__cap_\"^{TKeyValueObserver}}}"
- " '%@'"
- " -- fpItem: %p"
- " {raw: '%@'}"
- "%@(%@)"
- ", '%@'"
- "{TPrivateNodeInstantiationEnabler=\"fVolumeInfoPtr\"{shared_ptr<TFSVolumeInfo>=\"__ptr_\"^{TFSVolumeInfo}\"__cntrl_\"^{__shared_weak_count}}\"fFSInfo\"{shared_ptr<TFSInfo>=\"__ptr_\"^{TFSInfo}\"__cntrl_\"^{__shared_weak_count}}\"fAliasTarget\"{TNodePtr=\"fFINode\"@\"FINode\"}\"fOperationLock\"{unique_ptr<TOperationLock, std::default_delete<TOperationLock>>=\"__ptr_\"^{TOperationLock}}\"fParent\"^{TNode}\"fChildrenList\"{unique_ptr<TChildrenList, std::default_delete<TChildrenList>>=\"__ptr_\"^{TChildrenList}}\"fCustomNode\"^v\"fNotifierList\"{unique_ptr<TNotifierList, std::default_delete<TNotifierList>>=\"__ptr_\"^{TNotifierList}}\"fOpenSyncSignpost\"{unique_ptr<AutoSignpostInterval_General_OpenSync, std::default_delete<AutoSignpostInterval_General_OpenSync>>=\"__ptr_\"^{AutoSignpostInterval_General_OpenSync}}\"fFlags\"{atomic<unsigned short>=\"__a_\"{__cxx_atomic_impl<unsigned short, std::__cxx_atomic_base_impl<unsigned short>>=\"__a_value\"AS}}}"
- "{unique_ptr<AutoSignpostInterval_FPProvider_Gathering, std::default_delete<AutoSignpostInterval_FPProvider_Gathering>>=\"__ptr_\"^{AutoSignpostInterval_FPProvider_Gathering}}"
- "{unordered_map<NSProgress *, TKeyValueObserver, std::hash<NSProgress *>, std::equal_to<NSProgress *>, std::allocator<std::pair<NSProgress *const, TKeyValueObserver>>>=\"__table_\"{__hash_table<std::__hash_value_type<NSProgress *, TKeyValueObserver>, std::__unordered_map_hasher<NSProgress *, std::__hash_value_type<NSProgress *, TKeyValueObserver>, std::hash<NSProgress *>, std::equal_to<NSProgress *>>, std::__unordered_map_equal<NSProgress *, std::__hash_value_type<NSProgress *, TKeyValueObserver>, std::equal_to<NSProgress *>, std::hash<NSProgress *>>, std::allocator<std::__hash_value_type<NSProgress *, TKeyValueObserver>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
- "{unordered_map<NSURL *, std::pair<NSProgress *, TNSWeakPtr<FINode>>, std::hash<NSURL *>, std::equal_to<NSURL *>, std::allocator<std::pair<NSURL *const, std::pair<NSProgress *, TNSWeakPtr<FINode>>>>>=\"__table_\"{__hash_table<std::__hash_value_type<NSURL *, std::pair<NSProgress *, TNSWeakPtr<FINode>>>, std::__unordered_map_hasher<NSURL *, std::__hash_value_type<NSURL *, std::pair<NSProgress *, TNSWeakPtr<FINode>>>, std::hash<NSURL *>, std::equal_to<NSURL *>>, std::__unordered_map_equal<NSURL *, std::__hash_value_type<NSURL *, std::pair<NSProgress *, TNSWeakPtr<FINode>>>, std::equal_to<NSURL *>, std::hash<NSURL *>>, std::allocator<std::__hash_value_type<NSURL *, std::pair<NSProgress *, TNSWeakPtr<FINode>>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSURL *, std::pair<NSProgress *, TNSWeakPtr<FINode>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSURL *, std::pair<NSProgress *, TNSWeakPtr<FINode>>>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSURL *, std::pair<NSProgress *, TNSWeakPtr<FINode>>>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<NSURL *, std::pair<NSProgress *, TNSWeakPtr<FINode>>>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
- "{unordered_set<FINode *, std::hash<FINode *>, std::equal_to<FINode *>, std::allocator<FINode *>>=\"__table_\"{__hash_table<FINode *, std::hash<FINode *>, std::equal_to<FINode *>, std::allocator<FINode *>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<FINode *, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<FINode *, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<FINode *, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<FINode *, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
- "{unordered_set<NSObject *__unsafe_unretained, std::hash<NSObject *__unsafe_unretained>, std::equal_to<NSObject *__unsafe_unretained>, std::allocator<NSObject *__unsafe_unretained>>=\"__table_\"{__hash_table<NSObject *__unsafe_unretained, std::hash<NSObject *__unsafe_unretained>, std::equal_to<NSObject *__unsafe_unretained>, std::allocator<NSObject *__unsafe_unretained>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<NSObject *__unsafe_unretained, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<NSObject *__unsafe_unretained, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<NSObject *__unsafe_unretained, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<NSObject *__unsafe_unretained, void *> *>=\"__next_\"^v}\"__size_\"Q\"__hasher_\"{hash<NSObject *__unsafe_unretained>=\"fHash\"{hash<NSObject *>=}}\"__max_load_factor_\"f\"__key_eq_\"{equal_to<NSObject *__unsafe_unretained>=\"fEqual\"{equal_to<NSObject *>=}}}}"
- "{vector<NSObject<FINodeIterator> *, std::allocator<NSObject<FINodeIterator> *>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}"
- "{vector<TKeyValueObserver, std::allocator<TKeyValueObserver>>=\"__begin_\"^{TKeyValueObserver}\"__end_\"^{TKeyValueObserver}\"__cap_\"^{TKeyValueObserver}}"

```
