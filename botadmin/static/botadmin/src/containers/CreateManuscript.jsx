import ManuscriptForm from "../components/ManuscriptForm";
import { connect } from "react-redux";
import {
  addManuscript, addManuscriptItem, changeManuscriptItemProperty, changeManuscriptProperty,
  deleteManuscriptItem, moveManuscriptItem, postManuscript
} from "../actions/manuscripts";
import { loadAndDispatchManuscripts, sendManuscriptToApi } from "../utils/manuscript";
import { getManuscriptsApiUrl } from "../utils/urls";
import * as toastr from "toastr";
import { createManuscript } from "../actions/current_manuscript";

const mapStateToProps = (state) => {
  return {
    manuscript: state.current_manuscript,
    manuscripts: state.manuscripts
  };
};

const mapDispatchToProps = (dispatch, { history }) => {
  dispatch(createManuscript());
  loadAndDispatchManuscripts(dispatch).then(() => {
    dispatch(addManuscript());
    dispatch(addManuscriptItem(-1));
  });
  return {
    addManuscriptItem: () => {
      dispatch(addManuscriptItem(-1));
    },
    changeManuscriptProperty: (event, propertyName) => {
      dispatch(changeManuscriptProperty(-1, propertyName, event.target.value));
    },
    changeManuscriptItemProperty: (event, order, propertyName) => {
      dispatch(changeManuscriptItemProperty(-1, order, propertyName, event.target.value));
    },
    deleteManuscriptItem: (order) => {
      if (window.confirm('Are you sure?')) {
        dispatch(deleteManuscriptItem(-1, order));
      }
    },
    moveManuscriptItemDown: (order) => {
      dispatch(moveManuscriptItem(-1, order, 1));
    },
    moveManuscriptItemUp: (order) => {
      dispatch(moveManuscriptItem(-1, order, -1));
    },
    onSubmit: (event, manuscript) => {
      event.preventDefault();
      dispatch(postManuscript(manuscript));
      const timeoutHandleId = setTimeout(() => toastr.info('Trying to save manuscript, please wait'), 300);
      return sendManuscriptToApi(manuscript, getManuscriptsApiUrl(), 'POST')
        .then(createdManuscript => {
          clearTimeout(timeoutHandleId);
          dispatch(postManuscript(manuscript, createdManuscript));
          history.push(`/edit/${createdManuscript.pk}`);
          toastr.success('Successfully created manuscript, navigated you to edit-mode');
        })
        .catch(error => {
          dispatch(postManuscript(manuscript, error));
          toastr.error('Failed to create manuscript');
        });
    },
    onTabSelect: (key) => {
      history.push(`/create?tab=${key}`)
    }
  }
};

const CreateManuscript = connect(
  mapStateToProps,
  mapDispatchToProps
)(ManuscriptForm);

export default CreateManuscript;
