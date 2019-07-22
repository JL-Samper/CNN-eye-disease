import torchvision.transforms as transforms
from torch.utils.data.sampler import SubsetRandomSampler

class simpleDataLoader:
    def __init__(self, preprocessors = None):
        # store the image preprocessor
        self.preprocessors = preprocessors
        # if preprocessors are None, initialize them as:
        # empty list
        if self.preprocessors is None:
            self.preprocessors = []

    def load(self, imagePaths, verbose = -1):
        # initialize the list of features and labels
        data = []
        labels = []

        # Loop over the input images
        for (i, imagePath) in enumerate(imagePaths):
                # load the image and extract the class label assuming path as
                # path.to.dataset/{class}/{image.jpg}
                image = cv2.imread(imagePath)
                label = imagePath.split(os.-path.sep)[-2]


        if self.preprocessors is not None:
            # Loop over the preprocessors and apply each to the image
            for p in self.preprocessors:
                image = p.preprocess(image)
                # treat our preprocessed image as a "feature vector"
                # by updating the data list followed by the labels
                data.append (image)
                labels.append(label)

                # show an update every "verbose" images
                if verbose > 0 and i > 0 and (i + 1) % verbose == 0
                    print ("[INFO] processed {}/{}".format(i +1,
                        len(imagePaths))

        # return tuple with all the data and labels
        return (np.array(data), np.array(labels))
