## ProactiveSupport

> `/System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport`

```diff

 415.1.0.0.0
-  __TEXT.__text: 0x62ce0
+  __TEXT.__text: 0x62d30
   __TEXT.__auth_stubs: 0x2120
   __TEXT.__objc_methlist: 0x3da4
   __TEXT.__const: 0xcf3

   __TEXT.__eh_frame: 0x4a8
   __TEXT.__objc_classname: 0x98b
   __TEXT.__objc_methname: 0x8e31
-  __TEXT.__objc_methtype: 0x1a71
+  __TEXT.__objc_methtype: 0x1a83
   __TEXT.__objc_stubs: 0x61c0
   __DATA_CONST.__got: 0x638
   __DATA_CONST.__const: 0x19e0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 0ED38DEA-AAE1-3AAC-B5B9-740E65500DF6
+  UUID: 375238AC-75A7-3235-BC76-D8B8411593E1
   Functions: 1934
   Symbols:   6224
   CStrings:  3518
Functions:
~ -[NSString(_PASAdditions) _pas_stringBackedByUTF8CString] : 668 -> 688
~ +[NSIndexPath(_PASAdditions) _pas_fromVersionString:withExceptions:] : 1084 -> 1104
~ -[NSSet(_PASAdditions) _pas_setByRemovingObjectsFromSet:] : 640 -> 660
~ -[_PASSQLColumnMapping indexForColumnName:table:] : 640 -> 660
CStrings:
+ "{HDGuardedData=\"scores\"{SimdVector<float __attribute__((ext_vector_type(8))), float>=\"chunks\"{vector<float __attribute__((ext_vector_type(8))), (anonymous namespace)::SimdAlignedAllocator<float __attribute__((ext_vector_type(8)))>>=\"__begin_\"^\"__end_\"^\"\"{?=\"__cap_\"^}}\"count\"Q}\"abs\"{SimdVector<int __attribute__((ext_vector_type(8))), unsigned int>=\"chunks\"{vector<int __attribute__((ext_vector_type(8))), (anonymous namespace)::SimdAlignedAllocator<int __attribute__((ext_vector_type(8)))>>=\"__begin_\"^\"__end_\"^\"\"{?=\"__cap_\"^}}\"count\"Q}\"enumerationInProgress\"B}"
+ "{unique_ptr<proactive::pas::SynchronizedObject<(anonymous namespace)::HDGuardedData, proactive::pas::detail::RecursiveMutex>, std::default_delete<proactive::pas::SynchronizedObject<(anonymous namespace)::HDGuardedData, proactive::pas::detail::RecursiveMutex>>>=\"\"{?=\"__ptr_\"^v}}"
- "{HDGuardedData=\"scores\"{SimdVector<float __attribute__((ext_vector_type(8))), float>=\"chunks\"{vector<float __attribute__((ext_vector_type(8))), (anonymous namespace)::SimdAlignedAllocator<float __attribute__((ext_vector_type(8)))>>=\"__begin_\"^\"__end_\"^\"__cap_\"^}\"count\"Q}\"abs\"{SimdVector<int __attribute__((ext_vector_type(8))), unsigned int>=\"chunks\"{vector<int __attribute__((ext_vector_type(8))), (anonymous namespace)::SimdAlignedAllocator<int __attribute__((ext_vector_type(8)))>>=\"__begin_\"^\"__end_\"^\"__cap_\"^}\"count\"Q}\"enumerationInProgress\"B}"
- "{unique_ptr<proactive::pas::SynchronizedObject<(anonymous namespace)::HDGuardedData, proactive::pas::detail::RecursiveMutex>, std::default_delete<proactive::pas::SynchronizedObject<(anonymous namespace)::HDGuardedData, proactive::pas::detail::RecursiveMutex>>>=\"__ptr_\"^v}"

```
