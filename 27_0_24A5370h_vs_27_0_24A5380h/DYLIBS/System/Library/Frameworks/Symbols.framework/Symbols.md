## Symbols

> `/System/Library/Frameworks/Symbols.framework/Symbols`

```diff

   __AUTH_CONST.__objc_const: 0x1428
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x1d8
-  __AUTH.__objc_data: 0x1e0
+  __AUTH.__objc_data: 0x370
   __DATA.__objc_ivar: 0x94
   __DATA.__data: 0x300
   __DATA.__common: 0x10
   __DATA.__bss: 0x1d00
-  __DATA_DIRTY.__objc_data: 0x410
+  __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__bss: 0x480
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __DATA.__data : content changed
Functions:
~ +[NSSymbolDisappearEffect disappearDownEffect] -> -[NSSymbolEffectOptions .cxx_destruct] : 80 -> 12
~ +[NSSymbolDisappearEffect effect] -> +[NSSymbolDisappearEffect disappearDownEffect] : 84 -> 80
~ +[NSSymbolEffect _effectWithType:] -> +[NSSymbolDisappearEffect effect] : 56 -> 84
~ -[NSSymbolDisappearEffect _withStyle:] -> +[NSSymbolEffect _effectWithType:] : 8 -> 56
~ +[NSSymbolEffectOptions options] -> -[NSSymbolDisappearEffect _withStyle:] : 112 -> 8
~ -[NSSymbolEffectOptions set_speed:] -> +[NSSymbolEffectOptions options] : 8 -> 112
~ -[NSSymbolEffectOptions set_repeatDelay:] -> -[NSSymbolEffectOptions set_repeatCount:] : 12 -> 8
~ -[NSSymbolEffect _effectType] -> -[NSSymbolEffectOptions set_repeatDelay:] : 8 -> 12
~ -[NSSymbolDisappearEffect copyWithZone:] -> -[NSSymbolEffect _effectType] : 84 -> 8
~ -[NSSymbolEffect copyWithZone:] -> -[NSSymbolDisappearEffect copyWithZone:] : 60 -> 84
~ -[NSSymbolEffectOptions copyWithZone:] -> -[NSSymbolEffect copyWithZone:] : 184 -> 60
~ -[NSSymbolEffectOptions _speed] -> -[NSSymbolEffectOptions copyWithZone:] : 8 -> 184
~ -[NSSymbolEffectOptions .cxx_destruct] -> -[NSSymbolDisappearEffect _style] : 12 -> 8

```
