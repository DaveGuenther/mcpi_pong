# this file is used to define global functions related to class management or messageing 

def type_error_message(required_class, found_class):
    err_msg = "Required object of type <class "+str(required_class.__module__)+"."+str(required_class.__name__)+">.  Found object of type "+str(type(found_class))+" instead."
    return err_msg

def isinstance(instance, class_def):
    """
    Unlike the standard isinstance() function, this one will only check that the __name__ feature of both classes match.  The purpose for this is that unittesting requires a fake mcpi Minecraft object to be used.  The fake class is also called Minecraft.  The standard isinstance() function will fail, where this one will pass because it will only check the __name__ attributes of each for a match.
    """
    return instance.__class__.__name__==class_def.__name__