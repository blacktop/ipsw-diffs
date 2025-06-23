## DiagnosticsKit

> `/System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit`

```diff

-70.0.0.0.0
-  __TEXT.__text: 0x1ebc0
+72.0.1.0.0
+  __TEXT.__text: 0x1f750
   __TEXT.__auth_stubs: 0x640
   __TEXT.__objc_methlist: 0x2eac
   __TEXT.__const: 0xe8
   __TEXT.__cstring: 0x1ac9
-  __TEXT.__oslogstring: 0x12ea
+  __TEXT.__oslogstring: 0x17c0
   __TEXT.__gcc_except_tab: 0xbc4
   __TEXT.__dlopen_cstrs: 0x173
-  __TEXT.__unwind_info: 0x960
+  __TEXT.__unwind_info: 0x970
   __TEXT.__objc_classname: 0x6ca
   __TEXT.__objc_methname: 0x5970
   __TEXT.__objc_methtype: 0x1080

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8885A61B-CEAF-3B52-9680-A9452C89D769
-  Functions: 925
-  Symbols:   3504
-  CStrings:  1657
+  UUID: 547FDABB-23FD-3FB8-BF2B-96F6418663F3
+  Functions: 940
+  Symbols:   3538
+  CStrings:  1672
 
Symbols:
+ -[NSDictionary(Validations) dk_arrayFromKey:inSet:maxLength:defaultValue:failed:].cold.1
+ -[NSDictionary(Validations) dk_arrayFromKey:inSet:maxLength:defaultValue:failed:].cold.2
+ -[NSDictionary(Validations) dk_arrayFromKey:types:maxLength:defaultValue:failed:validator:].cold.1
+ -[NSDictionary(Validations) dk_arrayFromKey:types:maxLength:defaultValue:failed:validator:].cold.2
+ -[NSDictionary(Validations) dk_arrayFromKey:types:maxLength:defaultValue:failed:validator:].cold.3
+ -[NSDictionary(Validations) dk_boolFromKey:defaultValue:failed:].cold.1
+ -[NSDictionary(Validations) dk_dataFromKey:minLength:maxLength:defaultValue:failed:].cold.1
+ -[NSDictionary(Validations) dk_dictionaryFromKey:defaultValue:failed:].cold.1
+ -[NSDictionary(Validations) dk_numberFromKey:lowerBound:upperBound:defaultValue:failed:].cold.1
+ -[NSDictionary(Validations) dk_stringFromKey:maxLength:defaultValue:failed:].cold.1
+ -[NSDictionary(Validations) dk_stringFromKey:maxLength:defaultValue:failed:].cold.2
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
CStrings:
+ "Input validation failed; value for key \"%@\" contains an unspecified element %@"
+ "Input validation failed; value for key \"%@\" custom validation failed"
+ "Input validation failed; value for key \"%@\" is longer than max length %lu"
+ "Input validation failed; value for key \"%@\" must be of class NSArray, but is %@"
+ "Input validation failed; value for key \"%@\" must be of class NSData, but is %@"
+ "Input validation failed; value for key \"%@\" must be of class NSDictionary, but is %@"
+ "Input validation failed; value for key \"%@\" must be of class NSNumber, but is %@"
+ "Input validation failed; value for key \"%@\" must be of class NSString, but is %@"
+ "Input validation failed; value for key \"%@\" must have a count less than %lu, but is %lu"
+ "Input validation failed; value for key \"%@\" must not be greater than %@, but is %@"
+ "Input validation failed; value for key \"%@\" must not be less than %@, but is %@"
+ "Input validation failed; value for key \"%@\" must not have a count greater than %lu, but is %lu"
+ "Input validation failed; value for key \"%@\" must not have a length greater than %lu, but is %lu"
+ "Input validation failed; value for key \"%@\" must not have a length less than %lu, but is %lu"
+ "Input validation failed; values in array with key \"%@\" must be of types %@"

```
