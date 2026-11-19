## Automator

> `/System/Library/Frameworks/Automator.framework/Versions/A/Automator`

```diff

-540.0.0.0.0
-  __TEXT.__text: 0x16dafc
+541.0.0.0.0
+  __TEXT.__text: 0x16da64
   __TEXT.__objc_methlist: 0x1e8b8
   __TEXT.__gcc_except_tab: 0x177c
   __TEXT.__const: 0x220
-  __TEXT.__cstring: 0x18ac8
+  __TEXT.__cstring: 0x177fe
+  __TEXT.__ustring: 0x22f6
   __TEXT.__oslogstring: 0x1a89
-  __TEXT.__ustring: 0x2a8
   __TEXT.__unwind_info: 0x6650
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_arraydata: 0x678
   __DATA_CONST.__got: 0x1098
   __AUTH_CONST.__const: 0x28f0
-  __AUTH_CONST.__cfstring: 0x1b840
+  __AUTH_CONST.__cfstring: 0x1b7e0
   __AUTH_CONST.__objc_const: 0x32370
   __AUTH_CONST.__objc_intobj: 0x768
   __AUTH_CONST.__objc_arrayobj: 0x480

   - /usr/lib/libobjc.A.dylib
   Functions: 10628
   Symbols:   20665
-  CStrings:  4081
+  CStrings:  4078
 
Functions:
~ -[AMVariablesRegistry calculateVariablesByCategory] : 1612 -> 1512
~ -[AMLibrary organizeAction:byKey:inGroup:] : 4640 -> 4588
CStrings:
+ "An error occurred while converting “%@” to “%@.”"
+ "Are you sure you want to remove the variable “%@” from your workflow?"
+ "Automator encountered an error running this workflow: “%@”"
+ "Automator saves Calendar Alarms in the Automator calendar. The Automator calendar can’t be modified because it is read-only. Please rename or remove the calendar."
+ "Custom format…"
+ "Delete “%@”"
+ "Edit…"
+ "Failed to resolve path “%@.”"
+ "Installing “%@”"
+ "New variable…"
+ "New…"
+ "No variable named “%@”"
+ "Other…"
+ "Replace the action with the current version of “%@” in the library."
+ "Specifies the current time in a variable. Can specify the name of the variable. Can also create a custom time format or choose from four date formats from the user’s International Date and Time format preferences."
+ "Specifies today’s date in a variable. Can specify the name of the variable. Can also choose from four date formats from the user’s International Date and Time format preferences."
+ "Spotlight failed to find the file named “%@.” Please make sure privacy has not been enabled for this file in System Settings."
+ "The action “%@” could not be imported because it already exists in the Library."
+ "The action “%@” could not be loaded because %@ is required."
+ "The action “%@” could not be loaded because an unknown error occurred."
+ "The action “%@” could not be loaded because it could not be located."
+ "The action “%@” could not be loaded because it is damaged or missing necessary resources."
+ "The action “%@” could not be loaded because it is not Universal."
+ "The action “%@” could not be loaded because it is not compatible with the current application."
+ "The action “%@” could not be loaded because its executable is not loadable."
+ "The action “%@” could not be loaded because the action “%@” was not found."
+ "The action “%@” could not be loaded because the application “%@” is the wrong version."
+ "The action “%@” could not be loaded because the application “%@” was not found."
+ "The action “%@” could not be loaded because the file “%@” was not found."
+ "The action “%@” could not be loaded because the required resources were not found."
+ "The action “%@” could not be loaded."
+ "The action “%@” could not be saved because one or more of its properties are invalid."
+ "The action “%@” encountered an error: “%@”"
+ "The action “%@” is deprecated and will not be added to the workflow."
+ "The action “%@” is deprecated."
+ "The action “%@” is provided by a third party. Third party actions must be explicitly enabled."
+ "The action “%@” was not loaded because it could not be checked for malware."
+ "The action “%@” was not loaded because it has an invalid signature."
+ "The action “%@” was not loaded because it is from an unidentified developer."
+ "The action “%@” was not loaded because it was detected as malware."
+ "The action “%@” was not supplied with the required data."
+ "The document “%@” could not be opened because it is damaged or incomplete."
+ "The document “%@” could not be opened because it was saved with a newer version of Automator."
+ "The folder action is installed and attached to “%@.”"
+ "The workflow was saved with a newer version of the action “%@.” Some behavior may have changed."
+ "The workflow was saved with an older version of the action “%@.” Some behavior may have changed."
+ "The workflow “%@” was not loaded because it could not be checked for malware."
+ "The workflow “%@” was not loaded because it has an invalid signature."
+ "The workflow “%@” was not loaded because it was detected as malware."
+ "This action is deprecated. Replace the action with the current version of “%@” in the library."
+ "This workflow contains the action “%@”, which is provided by a third party. Third party actions must be explicitly enabled"
+ "Today’s date"
+ "Unable to set value of “%@.”"
+ "“%@”"
+ "“%@” is a workflow downloaded from the internet. Are you sure you want to install it?"
+ "“%@” is a workflow downloaded from the internet. Are you sure you want to open it?"
+ "“%@” is already installed. Do you want to replace it?"
+ "“%@” is an action downloaded from the internet. Are you sure you want to install it?"
+ "“%@” is an action downloaded from the internet. Are you sure you want to load it?"
+ "“%@” is an action from an unidentified developer. Are you sure you want to load it?"
- "An error occurred while converting \\U201C%@\\U201D to \\U201C%@.\\U201D"
- "Are you sure you want to remove the variable \\U201C%@\\U201D from your workflow?"
- "Automator encountered an error running this workflow: \\U201C%@\\U201D"
- "Automator saves Calendar Alarms in the Automator calendar. The Automator calendar can\\U2019t be modified because it is read-only. Please rename or remove the calendar."
- "Custom format\\U2026"
- "Date \\U0026 Time"
- "Delete \\U201C%@\\U201D"
- "Edit\\U2026"
- "Failed to resolve path \\U201C%@.\\U201D"
- "Files \\U0026 Folders"
- "Installing \\U201C%@\\U201D"
- "New variable\\U2026"
- "New\\U2026"
- "No variable named \\U201C%@\\U201D"
- "Other\\U2026"
- "Replace the action with the current version of \\U201C%@\\U201D in the library."
- "Specifies the current time in a variable. Can specify the name of the variable. Can also create a custom time format or choose from four date formats from the user\\U02BCs International Date and Time format preferences."
- "Specifies today\\U02BCs date in a variable. Can specify the name of the variable. Can also choose from four date formats from the user\\U02BCs International Date and Time format preferences."
- "Spotlight failed to find the file named \\U201C%@.\\U201D Please make sure privacy has not been enabled for this file in System Settings."
- "Text \\U0026 Data"
- "The action \\U201C%@\\U201D could not be imported because it already exists in the Library."
- "The action \\U201C%@\\U201D could not be loaded because %@ is required."
- "The action \\U201C%@\\U201D could not be loaded because an unknown error occurred."
- "The action \\U201C%@\\U201D could not be loaded because it could not be located."
- "The action \\U201C%@\\U201D could not be loaded because it is damaged or missing necessary resources."
- "The action \\U201C%@\\U201D could not be loaded because it is not Universal."
- "The action \\U201C%@\\U201D could not be loaded because it is not compatible with the current application."
- "The action \\U201C%@\\U201D could not be loaded because its executable is not loadable."
- "The action \\U201C%@\\U201D could not be loaded because the action \\U201C%@\\U201D was not found."
- "The action \\U201C%@\\U201D could not be loaded because the application \\U201C%@\\U201D is the wrong version."
- "The action \\U201C%@\\U201D could not be loaded because the application \\U201C%@\\U201D was not found."
- "The action \\U201C%@\\U201D could not be loaded because the file \\U201C%@\\U201D was not found."
- "The action \\U201C%@\\U201D could not be loaded because the required resources were not found."
- "The action \\U201C%@\\U201D could not be loaded."
- "The action \\U201C%@\\U201D could not be saved because one or more of its properties are invalid."
- "The action \\U201C%@\\U201D encountered an error: \\U201C%@\\U201D"
- "The action \\U201C%@\\U201D is deprecated and will not be added to the workflow."
- "The action \\U201C%@\\U201D is deprecated."
- "The action \\U201C%@\\U201D is provided by a third party. Third party actions must be explicitly enabled."
- "The action \\U201C%@\\U201D was not loaded because it could not be checked for malware."
- "The action \\U201C%@\\U201D was not loaded because it has an invalid signature."
- "The action \\U201C%@\\U201D was not loaded because it is from an unidentified developer."
- "The action \\U201C%@\\U201D was not loaded because it was detected as malware."
- "The action \\U201C%@\\U201D was not supplied with the required data."
- "The document \\U201C%@\\U201D could not be opened because it is damaged or incomplete."
- "The document \\U201C%@\\U201D could not be opened because it was saved with a newer version of Automator."
- "The folder action is installed and attached to \\U201C%@.\\U201D"
- "The workflow \\U201C%@\\U201D was not loaded because it could not be checked for malware."
- "The workflow \\U201C%@\\U201D was not loaded because it has an invalid signature."
- "The workflow \\U201C%@\\U201D was not loaded because it was detected as malware."
- "The workflow was saved with a newer version of the action \\U201C%@.\\U201D Some behavior may have changed."
- "The workflow was saved with an older version of the action \\U201C%@.\\U201D Some behavior may have changed."
- "This action is deprecated. Replace the action with the current version of \\U201C%@\\U201D in the library."
- "This workflow contains the action \\U201C%@\\U201D, which is provided by a third party. Third party actions must be explicitly enabled"
- "Today\\U02BCs date"
- "Unable to set value of \\U201C%@.\\U201D"
- "\\U201C%@\\U201D"
- "\\U201C%@\\U201D is a workflow downloaded from the internet. Are you sure you want to install it?"
- "\\U201C%@\\U201D is a workflow downloaded from the internet. Are you sure you want to open it?"
- "\\U201C%@\\U201D is already installed. Do you want to replace it?"
- "\\U201C%@\\U201D is an action downloaded from the internet. Are you sure you want to install it?"
- "\\U201C%@\\U201D is an action downloaded from the internet. Are you sure you want to load it?"
- "\\U201C%@\\U201D is an action from an unidentified developer. Are you sure you want to load it?"
```
