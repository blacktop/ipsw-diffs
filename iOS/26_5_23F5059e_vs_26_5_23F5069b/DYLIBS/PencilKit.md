## PencilKit

> `/System/Library/Frameworks/PencilKit.framework/PencilKit`

```diff

-577.4.3.0.0
-  __TEXT.__text: 0x33da40
+577.4.4.0.0
+  __TEXT.__text: 0x33da0c
   __TEXT.__auth_stubs: 0x3280
   __TEXT.__objc_methlist: 0x253ec
   __TEXT.__const: 0x7804

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7620AC15-858F-3C93-A490-5E8F3E47DC83
+  UUID: 87BD04E7-1A67-3235-A22E-7606D2F08EEC
   Functions: 17249
   Symbols:   56737
   CStrings:  22910
Functions:
~ -[PKTextEffectsWindowObserver _updateCachedKeyWindowBounds] -> -[PKTextEffectsWindowObserver dealloc] : 248 -> 56
~ -[PKTextEffectsWindowObserver _handleKeyWindowDidChangeNotification:] -> -[PKTextEffectsWindowObserver _updateCachedKeyWindowBounds] : 232 -> 248
~ -[PKTextEffectsWindowObserver _handleSceneDidActivateNotification:] -> -[PKTextEffectsWindowObserver _handleKeyWindowDidChangeNotification:] : 204 -> 232
~ -[PKTextEffectsWindowObserver _handleTextEffectsWindowDidRotateNotification:] -> -[PKTextEffectsWindowObserver _handleSceneDidActivateNotification:] : 4 -> 204
~ ___68-[PKTextEffectsWindowObserver _installColorAppearanceTraitObserver:]_block_invoke -> -[PKTextEffectsWindowObserver _handleTextEffectsWindowDidRotateNotification:] : 240 -> 4
~ -[PKTextEffectsWindowObserver keyWindow] -> ___68-[PKTextEffectsWindowObserver _installColorAppearanceTraitObserver:]_block_invoke : 332 -> 240
~ -[PKTextEffectsWindowObserver observeValueForKeyPath:ofObject:change:context:] -> -[PKTextEffectsWindowObserver keyWindow] : 288 -> 332
~ -[PKTextEffectsWindowObserver dealloc] -> -[PKTextEffectsWindowObserver observeValueForKeyPath:ofObject:change:context:] : 108 -> 288

```
