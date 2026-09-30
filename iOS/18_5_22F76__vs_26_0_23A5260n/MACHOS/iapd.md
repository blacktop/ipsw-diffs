## iapd

> `/System/Library/PrivateFrameworks/IAP.framework/Support/iapd`

```diff

-2165.120.2.0.0
-  __TEXT.__text: 0xe1108
+2169.0.0.0.0
+  __TEXT.__text: 0xe1208
   __TEXT.__auth_stubs: 0x2160
   __TEXT.__objc_stubs: 0x4e80
   __TEXT.__init_offsets: 0x1c
   __TEXT.__objc_methlist: 0x1a4c
-  __TEXT.__const: 0x6bf0
-  __TEXT.__gcc_except_tab: 0x1408
+  __TEXT.__const: 0x6c00
+  __TEXT.__gcc_except_tab: 0x13f4
   __TEXT.__cstring: 0x142a0
-  __TEXT.__objc_methname: 0x5707
+  __TEXT.__objc_methname: 0x5713
   __TEXT.__objc_classname: 0x2c8
-  __TEXT.__objc_methtype: 0x1172
-  __TEXT.__unwind_info: 0x1978
+  __TEXT.__objc_methtype: 0xed4
+  __TEXT.__unwind_info: 0x1960
   __DATA_CONST.__auth_got: 0x10c8
   __DATA_CONST.__got: 0x9e8
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x8290
+  __DATA_CONST.__const: 0x8270
   __DATA_CONST.__cfstring: 0x7680
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x20

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 065616AE-DFE9-36FD-A8E7-05141FA765E1
-  Functions: 4038
+  UUID: 1E48ABFB-E382-3E9C-9104-F7C8BEA79DE5
+  Functions: 4045
   Symbols:   870
   CStrings:  4192
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEPKcm
- __Znwm
CStrings:
+ "copySessions"
+ "copySessionsForClientID:"
+ "copySessionsWithProtocolID:"
+ "{map<unsigned int, NSNumber *, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, NSNumber *> > >=\"__tree_\"{__tree<std::__value_type<unsigned int, NSNumber *>, std::__map_value_compare<unsigned int, std::__value_type<unsigned int, NSNumber *>, std::less<unsigned int> >, std::allocator<std::__value_type<unsigned int, NSNumber *> > >=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{map<unsigned short, IAPSession *, std::less<unsigned short>, std::allocator<std::pair<const unsigned short, IAPSession *> > >=\"__tree_\"{__tree<std::__value_type<unsigned short, IAPSession *>, std::__map_value_compare<unsigned short, std::__value_type<unsigned short, IAPSession *>, std::less<unsigned short> >, std::allocator<std::__value_type<unsigned short, IAPSession *> > >=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "sessions"
- "sessionsForClientID:"
- "sessionsWithProtocolID:"
- "{map<unsigned int, NSNumber *, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, NSNumber *> > >=\"__tree_\"{__tree<std::__value_type<unsigned int, NSNumber *>, std::__map_value_compare<unsigned int, std::__value_type<unsigned int, NSNumber *>, std::less<unsigned int> >, std::allocator<std::__value_type<unsigned int, NSNumber *> > >=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<unsigned int, NSNumber *>, void *> > >=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<unsigned int, std::__value_type<unsigned int, NSNumber *>, std::less<unsigned int> > >=\"__value_\"Q}}}"
- "{map<unsigned short, IAPSession *, std::less<unsigned short>, std::allocator<std::pair<const unsigned short, IAPSession *> > >=\"__tree_\"{__tree<std::__value_type<unsigned short, IAPSession *>, std::__map_value_compare<unsigned short, std::__value_type<unsigned short, IAPSession *>, std::less<unsigned short> >, std::allocator<std::__value_type<unsigned short, IAPSession *> > >=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<unsigned short, IAPSession *>, void *> > >=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<unsigned short, std::__value_type<unsigned short, IAPSession *>, std::less<unsigned short> > >=\"__value_\"Q}}}"

```
