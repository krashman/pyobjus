import ctypes
ctypes.CDLL("/System/Library/Frameworks/AppKit.framework/Versions/C/Resources/BridgeSupport/AppKit.dylib")

from pyobjus import autoclass

NSString = autoclass('NSString')
NSMutableArray = autoclass("NSMutableArray")

array = NSMutableArray().arrayWithCapacity_(5)
text_val_one = NSString().initWithUTF8String_("some text for NSMutableArray")
text_val_two = NSString().initWithUTF8String_("some other text for NSMutableArray")

# we add some objects to NSMutableArray
array.addObject_(text_val_one)
array.addObject_(text_val_one)
array.addObject_(text_val_two)

count = array.count()
print "count of array before object delete -->", count

# then we remove some of them
array.removeObjectAtIndex_(0)
array.removeObject_(text_val_two)

count = array.count()
print "count of array after object delete -->", count

returnedObject = array.objectAtIndex_(0)
value = returnedObject.UTF8String()
print "string value of returned object -->", value