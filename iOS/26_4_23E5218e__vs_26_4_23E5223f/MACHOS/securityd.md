## securityd

> `/usr/libexec/securityd`

```diff

-61901.100.281.0.1
-  __TEXT.__text: 0x27d0f4
+61901.100.286.0.0
+  __TEXT.__text: 0x27d474
   __TEXT.__auth_stubs: 0x4210
   __TEXT.__objc_stubs: 0x1cc60
   __TEXT.__objc_methlist: 0x15670
-  __TEXT.__const: 0x921
+  __TEXT.__const: 0x919
   __TEXT.__cstring: 0x214d6
   __TEXT.__objc_methname: 0x2cd98
-  __TEXT.__oslogstring: 0x2e6cb
+  __TEXT.__oslogstring: 0x2e8ea
   __TEXT.__swift5_typeref: 0x378
   __TEXT.__swift5_fieldmd: 0x120
   __TEXT.__objc_classname: 0x2555

   __TEXT.__swift5_types: 0x20
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x3c
-  __TEXT.__gcc_except_tab: 0xb448
+  __TEXT.__gcc_except_tab: 0xb464
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x6ea0
+  __TEXT.__unwind_info: 0x6ea8
   __TEXT.__eh_frame: 0xa58
   __DATA_CONST.__auth_got: 0x2118
   __DATA_CONST.__got: 0x1388

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 1D45B65F-035D-3E98-993C-1224185A34F9
+  UUID: 3AB49FF8-77B8-3519-B435-FDEB8883440D
   Functions: 9743
   Symbols:   1858
-  CStrings:  19887
+  CStrings:  19892
 
Functions:
~ sub_1000b7594 : 240 -> 348
~ sub_1000b7704 -> sub_1000b7770 : 1484 -> 1956
~ sub_1000b7e28 -> sub_1000b806c : 476 -> 792
CStrings:
+ "SecItemAttrLogger: Duplicate key found in g_key_definitions at index %zu: %@"
+ "SecItemAttrLogger: Duplicate value found in g_value_definitions at index %zu: %@"
+ "SecItemAttrLogger: Failed to initialize lookup dictionaries in SecItemAttrLogger"
+ "SecItemAttrLogger: Invalid number value for kSecMatchLimit"
+ "SecItemAttrLogger: Invalid string value for kSecMatchLimit, got %@"
+ "SecItemAttrLogger: Invalid type for kSecAttrSynchronizable: got %s"
+ "SecItemAttrLogger: Invalid type for kSecMatchLimit: expected CFString or CFNumber, got %s"
+ "SecItemAttrLogger: Invalid type for type field in keys/idnt class: expected CFString, got %s"
+ "SecItemAttrLogger: Invalid value for `type` keyValue: %@"
+ "SecItemAttrLogger: Invalid value for kSecAttrSynchronizable, got %@"
+ "SecItemAttrLogger: Invalid value passed for attr: %@, value: %@"
+ "SecItemAttrLogger: Missing dict params"
+ "SecItemAttrLogger: Missing operation name"
+ "SecItemAttrLogger: Type mismatch for key: expected CFString, got %s"
+ "SecItemAttrLogger: Type mismatch for value: expected CFString, got: %s for attr: %@"
+ "SecItemAttrLogger: Unknown or missing class for type field handling"
+ "SecItemAttrLogger: attr not found in definitions - attr name: %@"
- "Failed to extract integer from CFNumber for kSecMatchLimit"
- "Failed to initialize lookup dictionaries in SecItemAttrLogger"
- "Invalid type for kSecAttrSynchronizable: got %s"
- "Invalid type for kSecMatchLimit: expected CFString or CFNumber, got %s"
- "Key not found in definitions - Key name: %@"
- "Missing dict params"
- "Missing operation name"
- "Parent index mismatch for value - Key: %@, Value: %@"
- "Type mismatch for kSecAttrSynchronizable value: expected CFString, got %s"
- "Type mismatch for key: expected CFString, got %s"
- "Type mismatch for value: expected CFString, got %s - Key: %@, Value type: %s"
- "Unrecognized CFString value for kSecMatchLimit"

```
