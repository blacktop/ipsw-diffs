## UIIntelligenceIntents

> `/System/Library/PrivateFrameworks/UIIntelligenceIntents.framework/UIIntelligenceIntents`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-9127.1.5.0.0
-  __TEXT.__text: 0x2b0a4
+9127.1.7.0.0
+  __TEXT.__text: 0x2b0a0
   __TEXT.__objc_methlist: 0x774
   __TEXT.__const: 0x3bd8
   __TEXT.__constg_swiftt: 0x91c
Functions:
~ sub_2b4f50b14 -> sub_2b534bb14 : 2404 -> 2400
CStrings:
+ "Present Writing Tools result "
+ "The text to be inserted into the app’s active text field."
+ "Window number (stringified) of the window that hosts the target text field. When provided on macOS, the bridge activates that window (`makeKeyAndOrderFront:`) before starting Writing Tools so AppKit’s default `keyWindow.firstResponder` coordinator walk lands on the intended field — necessary when a transient popover has stolen key focus."
- "Present writing tools result "
- "The text to be inserted into the app's active text field."
- "Window number (stringified) of the window that hosts the target text field. When provided on macOS, the bridge activates that window (`makeKeyAndOrderFront:`) before starting Writing Tools so AppKit's default `keyWindow.firstResponder` coordinator walk lands on the intended field — necessary when a transient popover has stolen key focus."
```
