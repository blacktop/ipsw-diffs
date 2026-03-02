## ScreenTimeCore

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore`

```diff

-605.4.16.0.0
-  __TEXT.__text: 0xc3d88
+605.4.17.0.0
+  __TEXT.__text: 0xc3d9c
   __TEXT.__auth_stubs: 0x1630
   __TEXT.__objc_methlist: 0x92d8
   __TEXT.__const: 0x2410

   __TEXT.__unwind_info: 0x3068
   __TEXT.__eh_frame: 0x16e0
   __TEXT.__objc_classname: 0x1e50
-  __TEXT.__objc_methname: 0x18fd0
+  __TEXT.__objc_methname: 0x19000
   __TEXT.__objc_methtype: 0x2b21
   __TEXT.__objc_stubs: 0xe0e0
   __DATA_CONST.__got: 0xbf0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 424CA5D8-9186-3439-9A05-4726864522AA
+  UUID: 0B74B7E1-F83B-3A98-B9F9-65BB78620043
   Functions: 4765
   Symbols:   12559
   CStrings:  7287
Symbols:
+ +[STBlueprint _buildConfigurationsByDeclarationIdentifierFromBlueprint:excludingConfigurationTypes:error:]
+ +[STBlueprint _buildConfigurationsByDeclarationIdentifierFromBlueprint:excludingConfigurationTypes:error:].cold.1
+ +[STBlueprint _buildConfigurationsByDeclarationIdentifierFromBlueprint:excludingConfigurationTypes:error:].cold.2
+ -[STBlueprint declarationsExcludingConfigurationTypes:error:]
+ -[STBlueprint declarationsExcludingConfigurationTypes:error:].cold.1
+ -[STBlueprint declarationsExcludingConfigurationTypes:error:].cold.2
+ _objc_msgSend$_buildConfigurationsByDeclarationIdentifierFromBlueprint:excludingConfigurationTypes:error:
- +[STBlueprint _buildConfigurationsByDeclarationIdentifierFromBlueprint:error:]
- +[STBlueprint _buildConfigurationsByDeclarationIdentifierFromBlueprint:error:].cold.1
- +[STBlueprint _buildConfigurationsByDeclarationIdentifierFromBlueprint:error:].cold.2
- -[STBlueprint declarationsWithError:]
- -[STBlueprint declarationsWithError:].cold.1
- -[STBlueprint declarationsWithError:].cold.2
- _objc_msgSend$_buildConfigurationsByDeclarationIdentifierFromBlueprint:error:
Functions:
~ -[STBlueprint declarationsWithError:] -> -[STBlueprint declarationsExcludingConfigurationTypes:error:] : 780 -> 796
~ +[STBlueprint _buildConfigurationsByDeclarationIdentifierFromBlueprint:error:] -> +[STBlueprint _buildConfigurationsByDeclarationIdentifierFromBlueprint:excludingConfigurationTypes:error:] : 868 -> 872
CStrings:
+ "_buildConfigurationsByDeclarationIdentifierFromBlueprint:excludingConfigurationTypes:error:"
+ "declarationsExcludingConfigurationTypes:error:"
- "_buildConfigurationsByDeclarationIdentifierFromBlueprint:error:"
- "declarationsWithError:"

```
