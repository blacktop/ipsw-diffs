## UniformTypeIdentifiers

> `/System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers`

```diff

 879.4.10.0.0
-  __TEXT.__text: 0xc46c
-  __TEXT.__auth_stubs: 0x780
+  __TEXT.__text: 0xc100
+  __TEXT.__auth_stubs: 0x770
   __TEXT.__objc_methlist: 0x784
   __TEXT.__const: 0x170
-  __TEXT.__gcc_except_tab: 0x1354
-  __TEXT.__cstring: 0x2342
+  __TEXT.__gcc_except_tab: 0x1350
+  __TEXT.__cstring: 0x1e0d
   __TEXT.__oslogstring: 0x4fb
   __TEXT.__unwind_info: 0x688
   __TEXT.__objc_classname: 0x141

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x678
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x3d0
+  __AUTH_CONST.__auth_got: 0x3c8
   __AUTH_CONST.__const: 0x268
   __AUTH_CONST.__cfstring: 0x1f60
   __AUTH_CONST.__objc_const: 0x688

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E33EB08D-0B00-3CE0-96F1-B910A6370AD0
+  UUID: D074AA38-51B7-3C8E-B606-28C63831C7E2
   Functions: 222
-  Symbols:   1130
-  CStrings:  896
+  Symbols:   1129
+  CStrings:  892
 
Symbols:
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9nqe210106EPKvm
+ __ZNSt12length_errorC1B9nqe210106EPKc
+ __ZNSt3__120__throw_length_errorB9nqe210106EPKc
+ __ZNSt3__127__throw_bad_optional_accessB9nqe210106Ev
+ __ZNSt3__16vectorIP12UTTypeRecordNS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorIP12UTTypeRecordNS_9allocatorIS3_EEEC2B9nqe210106EmRKS2_
+ __ZNSt3__16vectorIP9objc_ivarNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorIcNS_9allocatorIcEEEC2B9nqe210106EmRKc
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
+ ____ZN22UniformTypeIdentifiers9ModelCodeL26getDeviceTypeWithModelCodeEP8NSStringRKNSt3__18optionalI15UTHardwareColorEENS0_7OptionsE_block_invoke.75
+ ___block_literal_global.68
+ ___block_literal_global.77
+ ___block_literal_global.79
+ ___block_literal_global.801
+ _objc_release_x28
+ _objc_retain_x27
- __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9foe210106EPKvm
- __ZNSt12length_errorC1B9foe210106EPKc
- __ZNSt3__120__throw_length_errorB9foe210106EPKc
- __ZNSt3__127__throw_bad_optional_accessB9foe210106Ev
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__16vectorIP12UTTypeRecordNS_9allocatorIS3_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorIP12UTTypeRecordNS_9allocatorIS3_EEEC2B9foe210106EmRKS2_
- __ZNSt3__16vectorIP9objc_ivarNS_9allocatorIS2_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorIcNS_9allocatorIcEEEC2B9foe210106EmRKc
- __ZSt28__throw_bad_array_new_lengthB9foe210106v
- ____ZN22UniformTypeIdentifiers9ModelCodeL26getDeviceTypeWithModelCodeEP8NSStringRKNSt3__18optionalI15UTHardwareColorEENS0_7OptionsE_block_invoke.76
- ___block_literal_global.69
- ___block_literal_global.78
- ___block_literal_global.80
- ___block_literal_global.803
- _objc_release_x27
- _objc_retain_x28
Functions:
~ ___UTFindCoreTypesConstantWithIdentifier : 476 -> 448
~ __UTIdentifierGetHashCode : 688 -> 608
~ __UTIdentifiersAreEqual : 1668 -> 1468
~ +[UTType(UTTagSpecification) typesWithTag:tagClass:conformingToType:] : 1020 -> 972
~ ___UTGetDeclarationStatusFromInfoPlist : 984 -> 944
~ __ZN22UniformTypeIdentifiers9ModelCodeL71getDeviceTypeWithModelCodeAndHardwareColorWithoutResolvingCurrentDeviceEP8NSStringRKNSt3__18optionalI15UTHardwareColorEE : 944 -> 928
~ +[UTType _typesWithIdentifiers:] : 1076 -> 1028
~ -[UTType _parentTypes] : 1152 -> 1044
~ __ZN22UniformTypeIdentifiers4TypeL35detachTypeRecordsInNonConstantTypesIU8__strongP12NSMutableSetIP6UTTypeEEEvT_ : 912 -> 800
~ -[UTType(Conformance) supertypes] : 1144 -> 1036
~ __UTIdentifierGetCanonicalRepresentation : 736 -> 648
CStrings:
+ "void withFastBuffer(NSUInteger, const FunctionType &) [ElementType = char, ArraySize = 1024UL, FunctionType = (lambda at /Library/Caches/com.apple.xbs/2FF5E443-6398-40C5-9466-C7B0709C20F1/TemporaryDirectory.3YU8WQ/Sources/UniformTypeIdentifiers/Framework/UTType.mm:1221:34)]"
+ "void withFastBuffer(NSUInteger, const FunctionType &) [ElementType = char, ArraySize = 1024UL, FunctionType = (lambda at /Library/Caches/com.apple.xbs/2FF5E443-6398-40C5-9466-C7B0709C20F1/TemporaryDirectory.3YU8WQ/Sources/UniformTypeIdentifiers/Framework/UTType.mm:886:37)]"
+ "void withFastBuffer(NSUInteger, const FunctionType &) [ElementType = char, ArraySize = 1024UL, FunctionType = (lambda at /Library/Caches/com.apple.xbs/2FF5E443-6398-40C5-9466-C7B0709C20F1/TemporaryDirectory.3YU8WQ/Sources/UniformTypeIdentifiers/Framework/UTType.mm:886:91)]"
- "/AppleInternal/Library/BuildRoots/4~CJlJugAAU0MMuDqfBl2w2voXuiwR8cjLXetDLw0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugAAU0MMuDqfBl2w2voXuiwR8cjLXetDLw0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugAAU0MMuDqfBl2w2voXuiwR8cjLXetDLw0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugAAU0MMuDqfBl2w2voXuiwR8cjLXetDLw0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "void withFastBuffer(NSUInteger, const FunctionType &) [ElementType = char, ArraySize = 1024UL, FunctionType = (lambda at /Library/Caches/com.apple.xbs/78BBACF3-3CB0-4954-81E9-E898314B706B/TemporaryDirectory.WChosj/Sources/UniformTypeIdentifiers/Framework/UTType.mm:1221:34)]"
- "void withFastBuffer(NSUInteger, const FunctionType &) [ElementType = char, ArraySize = 1024UL, FunctionType = (lambda at /Library/Caches/com.apple.xbs/78BBACF3-3CB0-4954-81E9-E898314B706B/TemporaryDirectory.WChosj/Sources/UniformTypeIdentifiers/Framework/UTType.mm:886:37)]"
- "void withFastBuffer(NSUInteger, const FunctionType &) [ElementType = char, ArraySize = 1024UL, FunctionType = (lambda at /Library/Caches/com.apple.xbs/78BBACF3-3CB0-4954-81E9-E898314B706B/TemporaryDirectory.WChosj/Sources/UniformTypeIdentifiers/Framework/UTType.mm:886:91)]"

```
