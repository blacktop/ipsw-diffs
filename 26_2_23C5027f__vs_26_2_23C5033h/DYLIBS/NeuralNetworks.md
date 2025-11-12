## NeuralNetworks

> `/System/Library/PrivateFrameworks/NeuralNetworks.framework/NeuralNetworks`

```diff

 148.0.0.0.0
-  __TEXT.__text: 0x2233f0
+  __TEXT.__text: 0x222454
   __TEXT.__auth_stubs: 0x41d0
   __TEXT.__objc_methlist: 0x1504
   __TEXT.__const: 0x1df98

   __TEXT.__unwind_info: 0x8bf8
   __TEXT.__eh_frame: 0xd680
   __TEXT.__objc_classname: 0x22a
-  __TEXT.__objc_methname: 0x502e
-  __TEXT.__objc_methtype: 0x264a
+  __TEXT.__objc_methname: 0x5036
+  __TEXT.__objc_methtype: 0x26aa
   __TEXT.__objc_stubs: 0x1100
   __DATA_CONST.__got: 0xd40
   __DATA_CONST.__const: 0x620

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3AB86D01-EBAA-37A7-A5BE-509EC8EE214F
+  UUID: 858C20FA-CE71-3B4E-82BE-0476263AF6F7
   Functions: 16215
-  Symbols:   13293
+  Symbols:   13295
   CStrings:  2413
 
CStrings:
+ "@24@0:8{unique_ptr<MIL::IRProgram, std::default_delete<MIL::IRProgram>>={?=^{IRProgram}}}16"
+ "@32@0:8{unique_ptr<MIL::IRProgram, std::default_delete<MIL::IRProgram>>={?=^{IRProgram}}}16@24"
+ "@40@0:8{unique_ptr<const MIL::IRValue, std::default_delete<const MIL::IRValue>>={?=^{IRValue}}}16@24@32"
+ "@48@0:8r^{IRListValueType=^^?}16{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}24"
+ "@48@0:8r^{IRTensorValueType=^^?}16{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}24"
+ "@48@0:8r^{IRValueType=^^?}16{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}24"
+ "@56@0:8{shared_ptr<MIL::IRFunction>=^{IRFunction}^{__shared_weak_count}}16{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}32"
+ "T{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}},R,N"
+ "T{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}},R,N,V_opsetName"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"\"{?=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16@0:8"
+ "{map<std::string, const MIL::IRValueType *, std::less<std::string>, std::allocator<std::pair<const std::string, const MIL::IRValueType *>>>=\"__tree_\"{__tree<std::__value_type<std::string, const MIL::IRValueType *>, std::__map_value_compare<std::string, std::__value_type<std::string, const MIL::IRValueType *>, std::less<std::string>>, std::allocator<std::__value_type<std::string, const MIL::IRValueType *>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{unique_ptr<MIL::IRArgument, std::default_delete<MIL::IRArgument>>={?=^{IRArgument}}}24@0:8@16"
+ "{unique_ptr<MIL::Location, std::default_delete<MIL::Location>>=\"\"{?=\"__ptr_\"^{Location}}}"
+ "{unique_ptr<MIL::Location, std::default_delete<MIL::Location>>={?=^{Location}}}16@0:8"
+ "{unique_ptr<const MIL::IRValue, std::default_delete<const MIL::IRValue>>={?=^{IRValue}}}24@0:8@\"SNNMILContext\"16"
+ "{unique_ptr<const MIL::IRValue, std::default_delete<const MIL::IRValue>>={?=^{IRValue}}}24@0:8@16"
+ "{unique_ptr<const MIL::IRValue, std::default_delete<const MIL::IRValue>>={?=^{IRValue}}}32@0:8^v16Q24"
+ "{unique_ptr<const MIL::IRValue, std::default_delete<const MIL::IRValue>>={?=^{IRValue}}}40@0:8^v16@24Q32"
+ "{unique_ptr<const MIL::IRValue, std::default_delete<const MIL::IRValue>>={?=^{IRValue}}}48@0:8@16@24Q32@40"
+ "{vector<std::shared_ptr<MIL::IROperation>, std::allocator<std::shared_ptr<MIL::IROperation>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}"
+ "{vector<std::string, std::allocator<std::string>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}"
- "@24@0:8{unique_ptr<MIL::IRProgram, std::default_delete<MIL::IRProgram>>=^{IRProgram}}16"
- "@32@0:8{unique_ptr<MIL::IRProgram, std::default_delete<MIL::IRProgram>>=^{IRProgram}}16@24"
- "@40@0:8{unique_ptr<const MIL::IRValue, std::default_delete<const MIL::IRValue>>=^{IRValue}}16@24@32"
- "@48@0:8r^{IRListValueType=^^?}16{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}24"
- "@48@0:8r^{IRTensorValueType=^^?}16{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}24"
- "@48@0:8r^{IRValueType=^^?}16{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}24"
- "@56@0:8{shared_ptr<MIL::IRFunction>=^{IRFunction}^{__shared_weak_count}}16{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}32"
- "T{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})},R,N"
- "T{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})},R,N,V_opsetName"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16@0:8"
- "{map<std::string, const MIL::IRValueType *, std::less<std::string>, std::allocator<std::pair<const std::string, const MIL::IRValueType *>>>=\"__tree_\"{__tree<std::__value_type<std::string, const MIL::IRValueType *>, std::__map_value_compare<std::string, std::__value_type<std::string, const MIL::IRValueType *>, std::less<std::string>>, std::allocator<std::__value_type<std::string, const MIL::IRValueType *>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "{unique_ptr<MIL::IRArgument, std::default_delete<MIL::IRArgument>>=^{IRArgument}}24@0:8@16"
- "{unique_ptr<MIL::Location, std::default_delete<MIL::Location>>=\"__ptr_\"^{Location}}"
- "{unique_ptr<MIL::Location, std::default_delete<MIL::Location>>=^{Location}}16@0:8"
- "{unique_ptr<const MIL::IRValue, std::default_delete<const MIL::IRValue>>=^{IRValue}}24@0:8@\"SNNMILContext\"16"
- "{unique_ptr<const MIL::IRValue, std::default_delete<const MIL::IRValue>>=^{IRValue}}24@0:8@16"
- "{unique_ptr<const MIL::IRValue, std::default_delete<const MIL::IRValue>>=^{IRValue}}32@0:8^v16Q24"
- "{unique_ptr<const MIL::IRValue, std::default_delete<const MIL::IRValue>>=^{IRValue}}40@0:8^v16@24Q32"
- "{unique_ptr<const MIL::IRValue, std::default_delete<const MIL::IRValue>>=^{IRValue}}48@0:8@16@24Q32@40"
- "{vector<std::shared_ptr<MIL::IROperation>, std::allocator<std::shared_ptr<MIL::IROperation>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
- "{vector<std::string, std::allocator<std::string>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"

```
